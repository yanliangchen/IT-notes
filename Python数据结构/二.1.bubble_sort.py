#!/usr/bin/python
# -*- coding:utf-8 -*-
# Python 3.5
#冒泡排序算法
#两两比较，如果反序则交换，直到没有反序记录为止

class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def bubble_sort_simple(self):
        #拿前面的元素向后挨个比较，如果当前的元素大于等于被比较的元素，则调换位置
        """
        最简单的交换排序，时间复杂度O(n^2)
        """
        lis = self.r
        #获得长度
        length = len(self.r)
        #目的是获得左边的元素索引
        for i in range(length):
            print(i)
            #获得右面元素的索引
            for j in range(i+1, length):
                print(j)
                #挨个比较 如果不大于 继续循环 如果大于则跳出里层循环 进入到外层循环 继续比较
                #length是临界点的原因是 最后一个只能在后面了 所以没有取到length+1
                if lis[i] > lis[j]:
                    self.swap(i, j)

    def bubble_sort(self):
        """
        冒泡排序，时间复杂度O(n^2)
        """
        #从后开始向前俩俩比较 交换位置
        lis = self.r
        length = len(self.r)
        for i in range(length):
            print(i)
            j = length-2
            print(j)
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                j -= 1
                print(j)
    def bubble_sort_advance(self):
        """
        冒泡排序改进算法，时间复杂度O(n^2)
        设置flag，当一轮比较中未发生交换动作，则说明后面的元素其实已经有序排列了。
        对于比较规整的元素集合，可提高一定的排序效率。
        """
        lis = self.r
        length = len(self.r)
        flag = True
        i = 0
        while i < length and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis[j + 1]:
                    self.swap(j, j + 1)
                    flag = True
                j -= 1
            i += 1

    def __str__(self):
        #排好序的结果
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([-5, -1, -2,6,-5])
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.bubble_sort_advance()
    print(sqlist)