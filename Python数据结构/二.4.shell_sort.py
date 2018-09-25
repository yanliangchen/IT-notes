#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Python 3.5
# 希尔排序
'''
希尔排序（Shell Sort）是插入排序的改进版本，其核心思想是将原数据集合分割成若干个子序列，然后再对子序列分别进行直接插入排序，使子序列基本有序，最后再对全体记录进行一次直接插入排序。
这里最关键的是跳跃和分割的策略，也就是我们要怎么分割数据，间隔多大的问题。通常将相距某个“增量”的记录组成一个子序列，这样才能保证在子序列内分别进行直接插入排序后得到的结果是基本有序而不是局部有序。下面的例子中通过：increment = int(increment/3)+1来确定“增量”的值。
希尔排序的时间复杂度为：O(n^(3/2))
'''

class SQList:
    def __init__(self, lis=None):
        self.r = lis
    def shell_sort(self):
        lis = self.r
        length =len(lis)
        # 定义
        increment = len(lis)
        # 长度大于1的时候进入循环 分割成若干个子列
        while increment > 1:
            increment = int(increment/3)+1
            #6个元素第一轮i=4 length=6  inc=3
            for i in  range(increment+1,length):
                #和第一个元素进行比较 如果小于
                if  lis[i] < lis[i - increment]:
                    #暂存
                    temp = lis[i]
                    #j =1 获得第一个元素实际的值的索引
                    j = i - increment
                    #对这个被分割的子列内部进行判断 如果j>0 并且暂存的元素temp
                    while j >= 0 and  temp < lis[j]:
                        #就是调换位置 因为i = j/1+incre/3 =4 就是i 把刚才空出来的位置给到j的索引元素
                        lis[j + increment] = lis[j]
                        j -= increment
                    #不满足的时候 直接插入 
                    lis[j+increment] = temp



s=SQList([111,2,5,9,3,24,1])
s.shell_sort()
