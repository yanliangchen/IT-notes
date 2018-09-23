#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Python 3.5
# 简单选择排序
'''
就是，对尚未完成排序的所有元素，从头到尾比一遍，记录下最小的那个元素的下标，也就是该元素的位置。再把该元素交换到当前遍历的最前面。
其效率之处在于，每一轮中比较了很多次，但只交换一次。因此虽然它的时间复杂度也是O(n^2)，但比冒泡算法还是要好一点。
'''

class SQList:
    def __init__(self, lis=None):
        self.r = lis
    def swap(self,i,j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp
    def select_sort(self):
        """
        简单选择排序， 时间复杂度0(n^
        :return:
        """
        lis = self.r
        length = len(self.r)
        # i为获取左面的元素也就是1个元素它的索引(所在的列表)
        for  i  in  range(length):
            mininum = i
            #为右面元素的索引
            for  j  in  range(i+1, length):
                #如果左面的元素大于右面的元素
                if lis[mininum] > lis[j]:
                    #索引调换位置
                    mininum = j
            # 如果比较的索引元素的位置不一样
            if i != mininum:
                # 那么调换位置
                self.swap(i, mininum)

    #打印实例化对象的时候 以字符串返回
    def __str__(self):
        ret = ""
        for i  in  self.r:
            ret += "%s" %i
        return  ret
if __name__ == '__main__':
    #测试用例
    sqllist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0])
    sqllist.select_sort()
    print(sqllist)

