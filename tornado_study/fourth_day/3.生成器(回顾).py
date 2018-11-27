#!encoding=utf-8
def  foo():
    yield  1
    yield  2
    yield  3

# 生成器对象
res = foo()
# 1种遍历生成器对象
# print(res.next())
# 2种 对对象进行迭代
# for  i  in  res:
#     print(i)


########################
def  foo():
    r1 = yield  1
    r2 = yield  2
    print(r1, r2)
    yield  3
# 唤醒生成器
resa=foo()
print(resa.next())
#唤醒加赋值
r2 = resa.send('r1')
print(r2)
r3 = resa.send('r2')
# print(r3)
