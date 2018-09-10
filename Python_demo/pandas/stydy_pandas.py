# -*- coding: utf-8 -*-
import  pandas as pd
import  numpy   as  np

'''
Pandas的两大核心数据结构
Series(一维数据)
Series的数据结构为“键值对”的形式 
键-->可以重复
'''
#通过numpy数组结构创建Serires
res = pd.Series(np.arange(4,10))
# print(res)

#通过python数组创建Serires,并指定索引
res_two  = pd.Series([11,12,14],index=['北京','上海','深圳'])


#通过字典创建Series
res_three = pd.Series({'北京':11,"上海":12,"深圳":14})

#与字典不通，Series允许索引重复
a = pd.Series([11, 12, 14],index=["北京","上海","上海"])


'''
DataFrame(多特征数据，既有行索引，又有列索引)
'''

#DataFrame 可以进行行索引 列索引  是Pandas中重要的数据结构
data_3_4  = pd.DataFrame(np.arange(10,22).reshape(3,4))
#打印第一行数据
# print(data_3_4[:1])
#打印第一列数据
# print(data_3_4[:][1])

# 创建一个3行4列的DataFrame类型数据
data_5_6 = pd.DataFrame(np.arange(10,22).reshape(3,4))
# 打印数据
# print(data_3_4)
# 打印第一行数据
# print(data_3_4[:1])
# 打印第一列数据
# print(data_3_4[:][0])

#DataFrame的属性
'''
./*.csv 内容
id 姓名 age
1   李   20
2   祖   18
3   闲   17
4   从   23
5   宇   24
'''
result = pd.read_csv("./*.csv")
'''
# 数据的形状
print(result.shape)
# 每列数据的 类型信息
print(result.dtypes)
# 数据的维数
print(result.ndim)
# 数据的索引(起/始/步长)
print(result.index)
# 打印每一列 属性的名称
print(result.columns)
#将数据放到数组中显示
print(result.values)
'''

'''
#打印前5个
print("-->前5个:")
print(result.head(5))
#打印后5个
print("-->后5个:")
print(result.tail(5))
#打印描述信息(实验中好用)
print("-->描述信息")
print(result.describe())
'''


'''
Panda数据读取(以csv为例)
'''
res_p = pd.read_csv('./*.csv',sep=',',names=None,usecols=None)
#filepath_or_buffer :文件路径(本地路径或url路径)
#sep: 分隔符
#names: 列索引的名字
#usecols: 指定读取的列名
#返回的类型: DataFrame

res_t = pd.read_csv('./*.csv')
# print(res_t)

#获取特定字段，特定数量的信息
# print(res_t['姓名'][0:6])

print("读取后返回的数据类型为-->",type(res_t))

#Dataframe通过布尔索引过滤数据
#布尔索引(查询) 找出年龄大于23岁的人
print(res_t['age']>23)

'''
###########小案例############
1. 对爬取下来的1000部电影信息放到excel表格里 .csv文件做一个分析
'''
IMDB_1000 = pd.read_csv("./IMDB-Movie-Data.csv")
#获取数据字段
print(IMDB_1000.dtypes)
#根据1000部典以评分进行降序排列，参数ascending,默认为True(升序)，这里为False(降序)
IMDB_1000.sort_values(by="Rating", ascending=False)
#时间最长的电影   Runtime(Minutes)为表格里的字段
print(IMDB_1000[IMDB_1000['Runtime(Minutes)']==IMDB_1000['Runtime(Minutes)'].max()])
print(IMDB_1000[IMDB_1000['Runtime(Minutes)']==IMDB_1000['Runtime(Minutes)'].min()])
#电影时长平均值
IMDB_1000['Runtime (Minutes)'].mean()

'''
数据处理
存在缺失值，直接删除数据(删除存在缺失值的样本)
'''
#删除存在缺失值的样本
IMDB_1000.dropna()
#不推荐的操作: 按列删除缺失值为IMDB_1000.dropna(axis=1)

#存在缺失值，直接填充数据fillna

# 为一些电影缺失的总票房添加平均值
IMDB_1000['Revenue (Millions)'].fillna(IMDB_1000["Revenue (Millions)"].mean(),inplace=True)


# 在线读取数据,并按照说明文档, 并对各列信息进行命名
bcw = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data", names=["Sample code number","Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape", "Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitoses","Class:"])

'''
小案例：日期格式转换 数据来源
'''
#读取前10行数据
train = pd.read_csv("./train.csv",nrows=10)
train['time'] = pd.to_datetime(train["time"],unit="s")
#将数据中的time转换为最小分度值为秒(s)的计量单位
# print(train)

#从日期中拆分出新的列 year,month,weekday
train['year'] = pd.DatetimeIndex(train['time']).year
train['month'] = pd.DatetimeIndex(train['time']).month
train['weekday'] = pd.DatetimeIndex(train['time']).weekday

'''
数据表的合并(merge)
'''

user_info = pd.read_csv("./user_info.csv")
'''
user_info.csv
user_id,姓名,age
1,徐三,23
2,徐四,22
3,宝儿,210
4,楚岚,21
5,王也,24
6,诸葛青,21
7,天师,89
8,吕梁,24
9,夏禾,26
'''
order_info = pd.read_csv("./order_info.csv")
'''
goods_info.csv
goods_id,goods_name
G10,三只松鼠
G12,MacBook
G13,iPad
G14,iPhone
'''
goods_info = pd.read_csv("./goods_info.csv")
'''
order_info.csv
order_id,use_id,goods_name
as789,1,三只松鼠
sd567,2,MacBook
hj456,4,iPad
'''
#合并字段-->user_id   以user_info 为主导，合并order_info  生成_uo
u_o = pd.merge(user_info,order_info,how="left",on=["user_id","user_id"])
u_o_g = pd.merge(u_o,goods_info,how="left",on=['goods_name',"goods_name"])


#读取3张表
user_info = pd.read_csv('./user_info.csv')
order_info = pd.read_csv('./order_info.csv')
goods_info = pd.read_csv('./goods_info.csv')

#合并三张表
u_o = pd.merge(user_info,order_info,how="left",on=['user_id',"user_id"])
u_o_g = pd.merge(u_o,goods_info,how="left",on=['goods_name','goods_name'])

#建立交叉表(用于计算分组的频率)
#交叉表，表示出用户姓名，和商品名之间的关系
user_goods = pd.crosstab(u_o_g['姓名'],u_o_g['goods_name'])
# print(user_goods)

#Pandas的分组和聚合(重要)
'''
小案例:星巴克全球分布情况 数据来源
'''
#统计每个国家星巴克的数量
starbucks = pd.read_csv('./directory.csv')
starbucks.groupby(['Country']).count()

#统计每个国家 每个省份 星巴克的数量
starbucks.groupby(["Country","State/Province"]).count()
starbucks = pd.read_csv("./directory.csv")

#全球各国家星巴克数量排名
starbuck_by_country = starbucks.groupby(['Country']).count().reset_index()
#全球各国starbuck店铺数量降序排序
starbuck_by_country.sort_values("Brand",ascending=False)


