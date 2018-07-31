#coding=utf-8
'''
1. 队列的特点
队列是一种有次序的数据集合，新数据项的添加总发生在尾端(rear)，而现存数据项的移除总发生在首端(front)
先进先出：First in First out(FIFO)，eg: 打印队列
队列仅有一个入口和一个出口，不允许数据项直接插入队中，也不允许从中
间移除数据项
2. 使用列表来模拟队列
假设队列要实现如下功能：
Queue():创建一个空队列对象，返回值为Queue对象;
enqueue(item):将数据项添加到队尾，无返回值;
dequeue():从队首移除数据项，返回值为队首数据项，队列被修改
isEmpty():测试是否空队列 ，返回值为布尔值；
size():返回队列中数据项的个数.
'''
#将list的首端作为队列的尾端，list的末端作为队列的首端
class Queue:
    def __init__(self):
        self.items=[]
        print(self.items)
    def  isEmpty(self):
        return  self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if  not self.isEmpty():
            return  self.items.pop()
    def size(self):
        return len(self.items)

#实例话一个队列对象
q=Queue()
#像队列里添加成员
q.enqueue(4)
#检测队列是否为空
print(q.isEmpty())
#查看队列的大小
print(q.size())
#从队列里删除成员 是从队列的右端移除尾部 （）
q.dequeue()
# 再次检测
print(q.isEmpty())
