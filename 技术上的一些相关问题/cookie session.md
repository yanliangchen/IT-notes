

### **1、cookie引入session：**

cookie看似解决了HTTP（短连接、无状态）的会话保持问题，但把全部用户数据保存在客户端，存在安全隐患，

于是cookie+session出现了！我们可以 把关于用户的数据保存在服务端，在客户端cookie里加一个sessionID（随机字符串），

基于以上原因：cook+session组合就此作古了单单使用cookie做会话保持的方式；

### **2、cookie+session的工作流程：**

(1)、当用户来访问服务端时,服务端生成一个随机字符串；

(2)、当用户登录成功后 把 {sessionID :随机字符串} 组织成键值对 加到 cookie里发送给用户；

(3)、服务器以发送给客户端 cookie中的随机字符串做键，用户信息做值，保存用户信息；

 

### **3、保存在服务端session数据格式**

{

 随机字符串                                        用户信息

傻狍子的随机字符串：        {id：1,nam："alex"，account：1000000000 }，

二狗子的随机字符串：        {id：1,nam："eric"，account：10}