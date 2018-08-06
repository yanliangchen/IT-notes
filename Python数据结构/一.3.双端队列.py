#coding=utf-8
'''
1. 双端队列的特点
双端队列是一种有次序的数据集，其首端和尾端都可以加入数据和移除数据
某种意义上说，双端队列集成了栈和队列的能力，但双端队列并不具有内在的LIFO或者FIFO特性，
如果用双端队列来模拟栈或队列，需要由使用者自行维护操作的一致性
2. 使用列表来模拟双端队列
假设栈要实现如下功能：
'''

class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    #查看队列
    def look(self):
        return self.items
    #加入到队首
    def addFront(self,item):
        self.items.append(item)
    #加入到队尾
    def addRear(self,item):
        self.items.insert(0,item)
    #从队首移除队员  可以看作 横着的队列 右面为首 左面为前
    def removeFront(self):
        if not self.isEmpty():
            return self.items.pop()
    def removeRear(self):
        if not self.isEmpty():
            return  self.items.pop(0)
    def size(self):
        return len(self.items)

#测试用例
if __name__ == '__main__':
    d=Deque()
    #检测为空，正确
    print(d.isEmpty())
    #从队列的前面进行添加
    d.addFront(1)
    d.addFront('2')
    print(d.size())
    #从队列的尾部进行添加
    d.addRear('3')
    print(d.size())
    print(d.look())
    print(d.removeFront())
    print(d.look())
    print(d.removeRear())
    print(d.look())
    print(d.size())