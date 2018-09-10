# -*- coding: utf-8 -*-
'''
摘自简书：https://www.jianshu.com/p/83c8ef18a1e8
'''
import  numpy  as  np
'''
1. Numpy创建简单的数组
'''
a = [[1, 2, 3, 4]]
# 将列表转换为数组
b = np.array(a)

'''
2.Numpy查看数组属性
'''
# 查看数组元素个数
# print(b.size)

# 查看数组形状
# print(b.shape)

# 查看数组维度
# print(b.ndim)

# 查看数组元素类型
# print(b.dtype)

'''
3.快速创建N维数组的api函数
'''
#创建10行10列的数值为浮点1的矩阵
# array_one = np.ones([10,10])
# print(array_one)

#创建10行10列的数值为浮点0的矩阵
array_zero = np.zeros([9,10])
# print(array_zero)

#从现有的数据/python列表/创建数组
a = [1,2,3]
#浅拷贝
arr1 = np.asarray(a)
#深拷贝
arr2 = np.array(a)
# print(arr1)

c =[[1,2,3],[4,5,6]]
arr3 =np.array(c)
# print(arr2.shape)

'''
4.Numpy创建随机数组
'''
'''
4.1均匀分布
'''
#创建指定形状(示例为10行10列)的数组(范围在0至1之间)
res  = np.random.rand(10,10)

#创建指定范围内的一个数
res2 = np.random.uniform(0,100)

#创建指定范围内的一个整数
res3 =np.random.randint(0,100)

'''
4.2正态分布
'''

#给定均值/标准差/维度的正态分布
#正态生成4行5列的二维数组
arr = np.random.normal(1.75,0.1,(4,5))

#数组的索引，切片
#截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]


#改变数组形状(要求前后元素个数匹配)
# print("reshape函数的使用")
#生成1行20列的数组
one_20 = np.zeros([20])
# print("-->1行20列<--")
#给1行20列的数组变成4行5列
one_4_5 = one_20.reshape([4,5])
# print("-->4行5列<--")
# print(one_4_5)


'''
5. Numpy计算(重要)
'''

'''
5.1 条件运算 
'''
#条件判断
stus_score = np.array([[80,88],[82,81],[84,75],[86,83],[75,81]])
#print(stus_score > 80)

#三目运算
#如果数值小于80,替换为0,如果大于80,替换为90
result  = np.where(stus_score<80,0,90)

'''
5.2 统计运算
'''

'''
5.2.1指定轴最大值amax(参数1：数组；参数2：axis=0/1; 0表示列1表示行)
'''

stus_score = np.array([[80,88] ,[82, 81], [84, 75], [86, 83], [75, 81]])
#求每一列的最大值(0表示列,1表示行)
max_every = np.amax(stus_score,axis=1)


'''
5.2.2 指定轴最小值min  
'''
stus_score = np.array([[80,88] ,[82, 81], [84, 75], [86, 83], [75, 81]])
#求每一列的最小值(0表示列)
min_every_lie = np.amin(stus_score,axis=0)
#求每一行的最小值(1表示行)
min_every_hang = np.amin(stus_score,axis=1)


'''
5.2.3 指定轴平均值mean
'''
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
#求每一列的平均值(0表示列)
avg_data = np.mean(stus_score,axis=0)

#求每一行的平均值(1表示行)
row_data = np.mean(stus_score,axis=1)

'''
5.2.4 方差std
'''
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
#求每一列的方差(0表示列)
#print("每一列的方差:")
row_std = np.std(stus_score,axis=0)

#求每一行的方差(1表示行)
#print("每一行的方差:")
column_std = np.std(stus_score,axis=1)



'''
6 .数组运算
'''
'''
6.1 数组与数的运算加法 
'''
stus_score = np.array([[80, 88], [82, 81], [84, 75,], [86, 83], [75, 81]])
# print("加分前：")
# print(stus_score)
# print('-----')
#通过索引按列查看stus_score
# print(stus_score[:,1])
# print('-----')
#为所有平时成绩都加5分
stus_score[:,0] =stus_score[:, 0]+5
# print(stus_score)
# print("加分后")


'''
6.2数组与数的运算：乘法
'''
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# print("减半前")
# print(stus_score)

#平时成绩减半
stus_score[:,0] = stus_score[:,0]*0.5
# print("减半后:")
# print(stus_score)

'''
6.3 数组间也支持加减乘除运算，但基本用不到
'''
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a + b
d = a - b
e = a * b
f = a / b
# print("a+b为",c)
# print("a-b为",d)
# print("a*b为",e)
# print("a/b为",f)

'''
7. 矩阵运算 np.dot()（非常重要）
'''
#                     体育平时成绩，体育期末成绩
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
#平时成绩占40% 期末成绩占60% 计算结果
q = np.array([[0.4],[0.6]])
resulta = np.dot(stus_score, q)
# print("最终结果为:",resulta)

'''
7.1 矩阵拼接
    矩阵垂直拼接
'''
# print("v1为:")
v1 = [[0,1,2,3,4,5],
      [6,7,8,9,10,11]]
# print(v1)

v2 = [[12, 13, 14, 15, 16, 17],
      [18, 19, 20, 21, 22, 23]]
# print(v2)
'''
7.1.1垂直拼接
'''
v_result  = np.vstack((v1,v2))
# print("v1和v2垂直拼接的结果为")
# print(v_result)

'''
7.1.2 矩阵水平拼接
'''
# print("v1为:")
v1 =[[0,1,2,3,4,5],
     [6,7,8,9,10,11]]
# print(v1)
# print("v2为")
v2 = [[12,13,14,15,16,17],
      [18,19,20,21,22,23]]
# print(v2)
#垂直拼接
result_h = np.hstack((v1,v2))
# print("v1和v2水平拼接的结果为")
# print(result_h)

'''
8. Numpy读取数据 np.genfromtxt
'''
#设置csv文件读取路径，设置分隔符
result_csv = np.genfromtxt("./*.csv",delimiter=",")
# print(result_csv)