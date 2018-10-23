#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Python 3.5
# 快速排序
# 思想参考,很详细:http://www.cnblogs.com/KuJo/p/8544775.html

import unittest


class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def quick_sort(self):
        """调用入口"""
        """参数: 两个哨兵low和high,起始位置和最后位置"""
        self.qsort(0, len(self.r) - 1)

    def qsort(self, low, high):
        """递归调用"""
        if low < high:
            """关键就是分别从左到右 和从右到左来进行和基准点比较 """
            pivot = self.partition(low, high)
            # 基准点的位置发生了变化之后  再次更换基准点 进行递归比较
            # 此时相当于之前的基准点在中间了  那我相当基准点两边的 两端数据进行再次成为基准点
            # 并且以之前的比较后算出来的基准点小的为结尾  大的为起始 进行递归比较  反反复复 到此over
            self.qsort(low, pivot - 1)
            self.qsort(pivot + 1, high)

    def partition(self, low, high):
        """
        快速排序的核心代码。
        其实就是将选取的pivot_key不断交换，将比它小的换到左边，将比它大的换到右边。
        它自己也在交换中不断变换自己的位置，直到完成所有的交换为止。
        但在函数调用的过程中，pivot_key的值始终不变。
        :param low:左边界下标
        :param high:右边界下标
        :return:分完左右区后pivot_key（基准点）所在位置的下标
        """
        lis = self.r
        # 基准点low的位置的值
        pivot_key = lis[low]
        while low < high:
            # 右面的哨兵high向左走
            # 大于等于基准点  证明顺序没问题 继续比较  （位置和条件同时满足继续）
            while low < high and lis[high] >= pivot_key:
                high -= 1
            # 不满足小于基准点情况下 调换位置
            self.swap(low, high)
            # 左面的哨兵向右走
            # 小于等于基准点 证明顺序没问题 继续比较 (位置和条件同时满足继续)
            while low < high and lis[low] <= pivot_key:
                low += 1
            # 不满足大于基准点情况下
            self.swap(low, high)
        return low

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

    def __iter__(self):
        return self.r


sqlist = SQList([5, 1, 8, 3, 313131, 5, 9, 2, 6, 513131, 123, 22])
sqlist.quick_sort()
lists = sqlist.__iter__()

# 测试代码


def division_funtion(sqlist):
    for i in range(0, len(sqlist) - 1):
        if sqlist[i] <= sqlist[i + 1]:
            return '没问题'


class TestDivision(unittest.TestCase):
    def test_int(self):
        self.assertEqual(division_funtion(lists), '没问题')
        print('快速排序好的列表是:', lists)


if __name__ == '__main__':
    unittest.main()
