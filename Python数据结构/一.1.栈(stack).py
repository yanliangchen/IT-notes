#usr/bin/python
#coding=utf-8
'''
1. 栈的特点
栈是一种有次序的数据项集合，在栈中，数据项的加入和移除都仅发
生在栈顶
后进先出：Last in First out(LIFO)，eg: word 中的 undo
反转次序
2. 使用列表来模拟栈
2.1 假设栈要实现如下功能：
stack():创建一个空栈，其中不包含任何数据项
push(item): 将item数据项加入栈顶,无返回值
pop():将栈顶数据项移除，返回栈顶的数据项，栈被修改
peek(): “窥视” 栈顶数据项,返回栈顶的数据项但不移除,栈不被修改
isEmpty():返回栈是否为空栈
size():返回栈中有多少个数据
'''

# 选用 List 的尾端（index=-1）作为栈顶，此时push/pop的复杂度为O(1)
# 若选用 List 的首端（index=0）作为栈顶，其push/pop的复杂度为O(n)，因为要用pop(0),insert(0,item)等来模拟出栈和入栈

class Stack:
    """使用 list 来模拟栈"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
#看栈是否为空,返回True或者是False
print(s.isEmpty())
#查看栈的大小
# print(s.size())
#向栈里添加数据（入栈）
s.push('1')
#进去的和出来的都是最外面也就是索引为最大
print(s.peek())
# s.peek = 'dog'
#查看移除的数据（出栈）
print(s.pop())




