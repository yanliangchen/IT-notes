介绍
""""""""

本章将介绍Jenkins Pipeline的所有方面，从运行Pipeline到写入Pipeline代码，甚至扩展Pipeline本身。

什么是 Pipeline
''''''''''''''''''''

Jenkins Pipeline是一套插件，支持将连续输送Pipeline实施和整合到Jenkins。Pipeline提供了一组可扩展的工具，用于通过PipelineDSL为代码创建简单到复杂的传送Pipeline。 

通常，此“Pipeline代码”将被写入 Jenkinsfile项目的源代码控制存储库，例如：

.. code-block:: none

    Jenkinsfile (Declarative Pipeline)
    pipeline {
        agent any
        stages {
            stage('Build') {
                steps {
                    sh 'make'
                }
            }
            stage('Test') {
                steps {
                    sh 'make check'
                    junit 'reports/**/*.xml'
                }
            }
            stage('Deploy') {
                steps {
                    sh 'make publish'
                }
            }
        }
    }

1. agent 表示 Jenkins 应该为 Pipeline 的着一部分分配一个执行者和工作区
2. stage 描述这条 Pipeline 的第一个阶段
3. steps 描述了要在其中运行的步骤 stage
4. sh 执行给定的 shell 命令
5. junit 是由 JUnit 插件提供的，用于聚合测试报告的 Pipeline 步骤

为什么是 Pipeline
''''''''''''''''''''''

Jenkins 从根本上讲是一种支持多种自动化模式的自动化引擎。Pipeline 在 Jenkins 上添加了一套强大的自动化工具，支持从简单的连续集成到全面的连续输送 Pipeline 的用例。通过建模一系列相关任务，用户可以利用 Pipeline 的许多功能：

    * 代码：Pipeline 以代码的形式体现，通常被检入源代码控制，是团队能够编辑，审查和迭代器传送流程。
    * 耐用：Pipeline 可以计划和计划外重新启动 Jenkins 管理时同时存在。
    * Pausable：Pipeline 可以选择停止并等待人工输入或批准，然后在继续 Pipeline 运行。
    * 多功能：Pipeline 支持复杂的现实世界连续交付要求，包括并行分叉/连接，勋和和执行工作的能力。
    * 可扩展：Pipeline 插件支持其 DSL 的自定义扩展以及与其他插件集成的多个选项。

虽然 Jenkins 一直允许基于形式的自由式工作联合起来的执行顺序任务，Pipeline 使这个概念成为 Jenkins 的最好的一个部分。
基于 Jenkins 的核心可扩展性，Pipeline 也可以由 Pipeline 共享库用户和插件开发人员扩展。
下面的流程图是在 Jenkins Pipeline 中容易建模的一个连续发货方案的示例：

.. include:: /images/jenkins/pipeline/Pipeline流量.png

Pipeline 条件
'''''''''''''''''''

step
^^^^^^^

单一任务，从基础中告诉了 Jenkins 应该怎么做。例如，要执行 shell 命令，请 ``make`` 使用一下 ``sh`` 步骤： ``sh 'make'`` 。当插件扩展 Pipeline DSL 时，通常意味着插件已经实现了一个新的步骤。

Node
^^^^^^^^

Pipeline 执行中的大部分工作都是一个或多个声明 ``node`` 步骤的上下文中完成的。将工作限制在 Node 步骤中有两件事情：

1. 通过将项目添加到 Jenkins 队列来带调度要运行的块中包含的步骤。一旦执行器在节点上空闲，步骤就会运行。2. 创建工作区（特定与该特定 Pipeline 的目录），可以从源代码控制中检出文件完成工作。

.. note::

    根据您的 Jenkins 配置，某些工作空间在一段时间不活动后可能无法自动清除。

Stage
^^^^^^^^^

``stage`` 是定义整个 Pipeline 的概念上不同子集的一个步骤，例如：“Build”，“Test”和“Deploy”，许多插件用于可视化或呈现Jenkins Pipeline 状态/进度。