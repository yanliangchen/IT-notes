#coding=utf-8
'''
1.链表简介:
链表是实现了数据之间保持逻辑顺序(通过引用实现)，但存储空间不必按顺序的方法
链表中的基本要素：
    节点：每一个节点有两个域，左边部份叫值域，用于存放用户数据；右边叫指针域，一般是存储着到下一个元素的指针(python 中使用引用来实现)
    head 节点：没有值域，只有指针域且永远指向第一个节点
    tail 节点：有值域，有指针域但永远指向 None
2.使用链表的好处
    插入删除速度很快，不用对整个链表进行调整
    能够动态的进行存储分配


3.使用类来模拟链表(待扩展...)
#假设链表要实现如下功能：
list():创建一个空列表
add(item):添加一个数据项列表中，假设item原先不存在于列表中
remove(item):从列表中移除item,列表被修改，item原先应存在于表中
search(item):在列表中查找item,返回布尔类型值
isEmpty():返回列表是否为空
size():返回列表包含了多少数据项
append(item):添加一个数据项列表末尾,假设item原先不存在于列表中
index(item):返回数据项在表中的位置
insert（pos,item):将数据项插入到位置pos,假设item原先不存在与列表中，同时原列表具有
足够多个数据项，能让item占据位置pos
pop():从列表末尾移除数据项，假设原列表至少有1个数据项
pop(pos):移除位置为pos的数据项，假设原列表存在位置pos
参考url:https://blog.csdn.net/mzpmzk/article/details/76087463
'''

#节点类
class  Node:
    def __init__(self,init_data):
        #初始化一个接收数据往里面做操作
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.next
    def get_next(self):
        return self.next
    def set_data(self,new_data):
        self.data =new_data
    def set_next(self,new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    # 从链表头插入对象
    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)  # 将链表头指向的下一个对象的地址赋给待插入对象
        self.head = temp          # 将待插入对象的地址赋给链表头

    # 遍历链表，取得其长度
    def size(self):
        #把链表的头给赋值到current
        current = self.head
        #初始一个数字0
        count = 0
        #wiile循环 也就是说链表不为空 证明它有长度
        while current != None:
            count = count + 1
            #获取头的下一个指向
            current = current.get_next()
        return count

    # 判断某元素是否在链表中
    def search(self,item):
        #初始化一个头部
        current = self.head
        #做个变量标记
        found = False
        while current != None and not found:
            #通过头部来获取数据  如果和我传入进来的相等
            # 则给found标记为True 循环结束(因为and必须要同时满足,or则有一个满足则就满足)
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    # 移除链表中的某个元素
    def remove(self,item):
        #让头的指向来判断
        current = self.head
        previous = None
        #标识变量
        found = False
        #进入循环
        while not found:
            #如果节点的数据为item传入进来的数据
            if current.get_data() == item:
                #结束循环
                found = True
            #否则继续循环
            else:
                #previous就不为空了
                #为current的上一个指向
                previous = current
                #current获取下一个指向作为当前current
                current = current.get_next()
        #如果current测试节点的指向为空
        if previous == None:
            #则current测试节点的下一个指向为头
              self.head = current.get_next()
        #如果current测试节点不为空
        else:
            #继续测试:cureeent测试节点的下一个指向
            previous.set_next(current.get_next())










