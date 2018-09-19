#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Python 3.5
# 直接插入排序
'''
直接插入排序（Straight Insertion Sort）:时间复杂度O(n^2)
基本操作是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表。
'''
class SQLList:
    def __init__(self,lis=None):
        self.r = lis
    def insert_sort(self):
        lis = self.r
        length = len(self.r)
        # 下标从1开始
        #【2，1，5】
        for i in range(1,length):
            # 如果当前元素小于前一个元素
            if lis[i] < lis[i-1]:
                # 那么把当前元素给到一个临时变量
                #1
                temp = lis[i]
                #j 前一个元素的索引
                #j 0
                j = i-1
                # 前一个元素 > 当前元素  并且j大于等于0
                #2 > 1  j 0
                while lis[j] > temp and j>=0:
                    #前一个元素后移
                    #满足条件 元素后移 索引为j+1
                    lis[j+1] = lis[j]
                    j -= 1
                # 不满足为前一个元素小于等于当前元素 则直接把当前元素给后移塞入进去
                lis[j+1] = temp