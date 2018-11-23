jenkinsfile 使用
"""""""""""""""""""""""

本节基于 “Jenkins 入门” 中介绍的信息，并介绍更有用的步骤，常见的模式，并演示一些非平凡的 Jenkinsfile 示例。

创建一个 Jenkinsfile 被检入源代码控制，提供了一些直接的好处：

* Pipeline 上的代码审查/迭代
* Pipeline 的审计跟踪
* Pipeline 的唯一真实来源，可以由项目的多个成员查看和编辑。

Pipeline 支持两种语法：Declarative（在 Pipeline 2.5 中引入）和 Scripted Pipeline。两者都支持建立连续输送 Pipeline。两者都可以用于在 Web UI 或者 a 中定义一个流水线 Jenkinsfile，尽管通常被认为是 Jenkinsfile 将文件创建并检查到源代码控制库中的最佳做法。

创建 Jenkinsfile
''''''''''''''''''''''

如”入门“部分所述， ``Jenkinsfile`` 是一个包含 Jenkins Pipeline 定义的文本文件，并被检入源代码控制，考虑以下 Pipeline，实施基本的三个阶段连续输送 Pipeline。

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    echo "Building.."
                }
            }
            stage('Test') {
                steps {
                    echo "Testing.."
                }
            }
            stage("Deploy") {
                steps {
                    echo "Deploying...."
                }
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    node {
        stage('build') {
            echo 'Building....'
        }
        stage('Test') {
            echo 'Testing....'
        }
        stage('Deploy') {
            echo 'Deploying....'
        }
    }


并非所有的 Pipeline 都将具有相同的三个阶段，但是对于大多数项目来说，这是一个很好的起点。以下部分将演示在 Jenkins 的测试安装中创建和执行简单的 Jenkins。

.. note:: 

    假设已经有一个项目的源代码管理库，并且已经在 Jenkins 中按照这些说明定义了一个 Jenkins。

使用文本编辑器，理想的是支持 Groovy 语法突出显示文本编辑器，项目的根目录中创建一个新的 Jenkinsfile。

上述声明性 Pipeline 示例包含实现连续传送 Pipeline 的最小必要结构。需要的代理指令指示 Jenkins 为 Pipeline 分配一个执行器和工作区。没有 agent 指令，不仅声明 Pipeline 无效，所以不能做任何工作！默认情况下，该 agent 伪指令确保源存储库已被检出并可用于后续阶段的步骤。

该阶段的指令，和步骤的指令也需要一个有效的声明 Pipeline，因为他们指示 Jenkins 如何执行并在哪个阶段应该执行。

.. note:: 

     要使用 Scripted Pipeline 进行更高级的使用，上面的示例 node 是为 Pipeline 分配执行程序和工作空间的关键第一步。在本质上，没有 node Pipeline 不能做的工作！从内部 node，业务的第一个顺序是检查此项目的源代码。由于 Jenkinsfile 直接从源代码控制中抽取，所以 Pipeline 提供了一种快速简便的方式来访问源代码的正确版本

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    node {
        checkout scm
        /* .. snip .. */
    }

checkout 步骤将检出从源控制代码；scm 是一个特殊边领，指示 checkout 步骤克隆触发此 Pipeline 运行的特定修订。

建立
'''''''''

对于许多项目，Pipeline “工作” 的开始就是“构建”阶段。通常，Pipeline 在这个阶段将是源代码组装，编译或打包的过程。Jenkinsfile 中有不是现有的构建工具，如 GNU/make，Maven，Gradle 等的替代品，而是可以被看作是一个胶层结合项目的开发生命周期的多个阶段（构建，测试，部署等）一起。

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    sh 'make'
                    archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
                }
            }
        }
    }

1. 该 sh 步骤调用 make 命令，只有在命令返回退出代码零时才会继续下一步。pipeline中任何不为零的退出代码都属于失败。
2. archiveArtifacts 捕获与 include pattern( ``**/target/*.jar`` ) 匹配文件，并将他们保存到 Jenkins 主文件以供后面检索。

.. attention:: 

    存档工件不能替代使用诸如 artifactory 或 Nexus 之类的外部工件存储库，只能用于基本报告和文件归档。

测试
''''''''

运行自动化测试是任何成功的连续传送过程的重要组成部分。因此，Jenkins 有许多插件提供的测试记录，报告和可视化设备。在基本层面上，当有测试失败时，让 Jenkins 在 Web UI 中记录报告和可视化的故障是有用的。下面的示例使用 junit 由 JUnit 插件提供的步骤。

在下面的示例中，如果测试失败，则Pipeline 被标记为“不稳定”，如 Web UI 中的黄色球。根据记录的测试报告，Jenkins 还可以提供历史趋势分析和可视化。

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any

        stages {
            steps {
                /* `make check` returns non-zero on test failures,
                * using `true` to allow the Pipeline to continue nonetheless
                */
                sh 'make check || true'
                junit '**/target/*.xml'
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    node {
        /* .. snip .. */
        stage('Test') {
            /* `make check` returns non-zero on test failures,
            * using `true` to allow the Pipeline to continue nonetheless
            */
            sh 'make check || true'
            junit '**/target/*.xml'
        }
        /* .. snip .. */
    }

1. 使用内联 shell conditional(sh 'make check || true') 确保该 sh 步骤始终看到退出代码零，从而使该 junit 步骤有机会捕获和处理测试报告。下面的“故障处理”部分将详细介绍其他方法。
2. junit 捕获并关联与包含 pattern( ``**/target/*.xml`` ) 匹配的 JUnit XML 文件

部署
'''''''''''''

部署可能意味着各种步骤，具体取决于项目或组织的要求，并且可能是从构建的工件发送到 Artifactory 服务器，将代码推送到生产系统的任何步骤。

在 Pipeline 示例的这个阶段，“构建”和“测试”阶段都已成功执行。实际上，“部署”阶段只能在上一阶段完成，否则 Pipeline 将提前退出。

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any

        stages {
            stage('Deploy') {
                when {
                    expression {
                        currentBuild.result == null || currentBuild.result == 'SUCCESS'
                    }
                }
                steps {
                    sh 'make publish'
                }
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    node {
        /* .. snip .. */
        stage('Deploy') {
            if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                sh 'make publish'
            }
        }
        /* .. snip .. */
    }

1. 访问该 ``currentBuild.result`` 变量允许 Pipeline 确定是否有任何测试失败。在这种情况下，值将是 ``UNSTABLE`` 。

假设一切都在 Jenkins Pipeline 示例中成功执行，每个成功的 Pipeline 运行都将会存档关联构建工件，报告的测试结果和完整的控制台输出全部放在 Jenkins 中。

.. note:: 

    脚本 Pipeline 可以包括条件测试（如上所示），循环，try/catch/finally 块甚至函数。下一节将详细介绍这种高级脚本 Pipeline 语法。

管道高级语法
''''''''''''''''

字符串插值
^^^^^^^^^^^^^

Jenkins Pipeline 使用于 Groovy 相同的规则进行字符串插值。Groovy 的字符串插值支持可能会让很多新来的语言搞到困惑。虽然 Groovy 支持使用单引号或双引号声明一个字符串，例如：

.. code-block:: none

    def singlyQuoted = 'Hello'
    def doublyQuoted = "World"

只有后一个字符串将支持基于 dollar-sign($) 的字符串插值，例如：

.. code-block:: none

    def username = 'Jenkins'
    echo 'Hello Mr. ${username}'
    echo "I said, Hello Mr. ${username}"

会导致

.. code-block:: none

    Hello Mr. ${username}
    I said, Hello Mr. Jenkins

了解如何使用字符串插值对于使用一些管道更高级的功能至关重要。


工作环境
''''''''''''''''

Jenkins Pipeline 通过全局变量公开环境变量，该变量 env 可以从任何地方获得 Jenkinsfile。假设 Jenkins 主机正在运行，在 http://localhost:8080/pipeline-syntax/globals#env 中记录了可从 Jenkins Pipeline 中访问的环境变量的完整列表 localhots:8080，其中包括：

* BUILD_ID

    当前版本ID，与 Jenkins 版本 1.597+ 中创建的构建相同，为 BUILD_NUMBER

* JOB_NAME

    此构建项目的名称，如 “foo” 或 “foo/bar”

* JENKINS_URL

    完整的 Jenkins 网址，例如 example.com:port/jenkins/ (注意：只有在“系统配置”中设置了 Jenkins 网址时才可用)

参考或使用这些环境变量可以像访问 Groovy Map 的任何键一样，例如：

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any
        stages {
            stage('Example') {
                steps {
                    echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                }
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    node {
        echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
    }

设置环境变量
^^^^^^^^^^^^^^

根据是否使用 Declarative 或 Scripted Pipeline，在 Jenkins Pipeline 中设置环境变量是不同的。
声明式 Pipeline 支持环境指令，而 Scripted pipeline 的用户必须使用该 withEnv 步骤。

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any
        environment {
            CC = 'clang'
        }

        stages {
            stage('Example') {
                environment {
                    DEBUG_FLAGS = '-g'
                }
                steps {
                    sh 'printenv'
                }
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    node {
        /* .. snip .. */
        withEnv(["PATH+MAVEN=${tool 'M3'}/bin"]) {
            sh 'mvn -B verify'
        }
    }

1. environment 顶级 pipeline 块中使用的指令将适用于 Pipeline 中的所有步骤。
2. 在一个 environment 意图中定义的一个指令 stage 仅将给定的环境变量应用与该过程中的步骤 stage

参数
''''''''

声明式 Pipeline 支持开箱即用的参数，允许 Pipeline 在运行时通过 parameters 指令接受用户指定的参数。使用脚本 Pipeline 配置参数是通过 properties 步骤完成的，可以在代码段生成器中找到。

如果你使用“使用参数构建”选项来配置 Pipeline 以接收参数，那么这些参数可作为 params 变量的成员访问。
假设一个名为 “Greeting” 的 String 参数已经在 Jenkinsfile 配置中，它可以通过 ${params.Greeting} 方式访问该参数，示例如下：

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any
        parameters {
            string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
        }
        stages {
            stage('Example') {
                steps {
                    echo "${params.Greeting} World!"
                }
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    properties([parameters([string(defaultValue: 'Hello', description: 'How should I greet the world?', name: 'Greeting')])])

    node {
        echo "${params.Greeting} World!"
    }

故障处理
'''''''''''

声明性 Pipeline 默认支持 robust 失败处理经由其 post section，其允许声明许多不同的 “post conditions”，例如：always，unstable，success，failure 和 changed。“Pipelne 语法” 部分提供了有关如何使用各种处置条件的更多详细信息。

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any
        stages {
            stage('Test') {
                steps {
                    sh 'make check'
                }
            }
        }
        post {
            always {
                junit '**/target/*.xml'
            }
            failure {
                mail to: team@example.com, subject: 'The Pipeline failed :('
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    node {
        /* .. snip .. */
        stage('Test') {
            try {
                sh 'make check'
            }
            finally {
                junit '**/target/*.xml'
            }
        }
        /* .. snip .. */
    }

但是脚本 Pipeline 依赖于 Groovy 的内置 try/catch/finally 该 pipeline 的执行过程中处理故障的语义。

在上面的测试示例中，该 sh 步骤被修改为从不返回非零退出代码（sh 'make check || true'）。这种方法虽然有效，但是意味着以下阶段需要检查 currentBuild。result 以确定是否测试失败。

处理这种情况的另一种方式是保留 Pipeline 故障的早期退出行为，同时仍然 junit 有机会补货测试报告，是使用一系列 try/finally 代码块

使用多个代理
''''''''''''''''''

在所有以前的例子中，值使用了一个代理。着意味着 Jenkins 将分配一个可用的执行器，无论他是如何标记或配置的。这不仅可以被行为覆盖，但 Pipeline 允许从内利用 Jenkins 环境中的多个代理商相同 Jenkinsfile，可为更高级的使用情况，如执行有帮助建立跨多个平台/测试。

在下面的示例中，“构建”阶段将在一个代理上执行，并且构建的结果将在“测试”阶段中分别标记为 “linux” 和 “windows” 的两个后续代理程序中重用。

.. code-block:: none 

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent none
        stages {
            stage('Build') {
                agent any
                steps {
                    checkout scm
                    sh 'make'
                    stash includes: '**/target/*.jar', name: 'app' 
                }
            }
            stage('Test on Linux') {
                agent { 
                    label 'linux'
                }
                steps {
                    unstash 'app' 
                    sh 'make check'
                }
                post {
                    always {
                        junit '**/target/*.xml'
                    }
                }
            }
            stage('Test on Windows') {
                agent {
                    label 'windows'
                }
                steps {
                    unstash 'app'
                    bat 'make check' 
                }
                post {
                    always {
                        junit '**/target/*.xml'
                    }
                }
            }
        }
    }

Toggle Scripted Pipeline (Advanced)

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    stage('Build') {
        node {
            checkout scm
            sh 'make'
            stash includes: '**/target/*.jar', name: 'app' 
        }
    }

    stage('Test') {
        node('linux') { 
            checkout scm
            try {
                unstash 'app' 
                sh 'make check'
            }
            finally {
                junit '**/target/*.xml'
            }
        }
        node('windows') {
            checkout scm
            try {
                unstash 'app'
                bat 'make check' 
            }
            finally {
                junit '**/target/*.xml'
            }
        }
    }

1. 该 ``stash`` 步骤允许捕获与包含模式（ ``**/target/*.jar`` ）匹配的文件，以在同一管道中重用。一旦 Pipeline 完成执行，垃圾文件将从 Jenkins 主站中删除。
2. agent 中的参数 ``node`` 允许任何有效的 Jenkins 标签表达式。
3. ``unstash`` 将从 Jenkins 主机当前工作空间中检索名为 app 的管道
4. 该 bat 脚本允许在基于 Windows 的平台上执行批处理脚本。

可选步骤参数
''''''''''''''''

Pipeline 尊许 Groovy 语言约定，允许在方法参数中省略括号。
许多 Pipeline 步骤还使用命名参数语法作为使用 Groovy 创建 map 的简写，它使用语法 [key1:value2, key2:value2]。发布如下功能的语句：

.. code-block:: none

    git url: 'git://example.com/amazing-project.git' branch: 'master'
    git([url: 'git://example.com/amazing-project.git', branch: 'master'])

为方便起见，当仅调用一个参数（或只有一个必须参数）时，可能会省略参数名称，例如：

.. code-block:: none

    sh 'echo hello' /* short form */
    sh([script: 'echo hello']) /* long form */

高级脚本管道
''''''''''''''

脚本 Pipeline 是基于 Groovy 的领域专用语言，大多数 Groovy 语法可以在脚本 Pipeline 中使用而无需修改。

同时执行
^^^^^^^^^^^

上面的例子在线性系列中的两个不同平台上运行测试。在实践中，如果 make cache 执行需要 30 分钟完成，“测试” 阶段现在需要 60 分钟才能完成！

幸运的时，Pipeline 具有内置功能，用于并执行 Scripted Pipeline 的部分，在适当命令的 Parallel 步骤中实现。重构上述示例以使用 parallel 步骤：

.. code-block:: none

    Jenkinsfile (Scripted Pipeline)
    stage('Build') {
        /* .. snip .. */
    }

    stage('Test') {
        parallel linux: {
            node('linux') {
                checkout scm
                try {
                    unstash 'app'
                    sh 'make check'
                }
                finally {
                    junit '**/target/*.xml'
                }
            }
        },
        windows: {
            node('windows') {
                /* .. snip .. */
            }
        }
    }

而不是在“linux”和“windows”标签的节点上执行测试，它们现在将在Jenkins环境中存在必需容量的情况下并行执行。