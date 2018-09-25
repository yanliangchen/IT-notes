#encoding=utf-8
def fibonacci():
    # 输入想要多少个项
    num = input(" your  number \n")
    i, a, b = 0, 0, 1
    if  int(num) < 0:
        print(u"你输入的数据不合理")
    elif int(num) == 1:
        print(a)
    else:
        while i < int(num):
            print(a,'a','-----',b,'b')
            #1. a起初始0 b初始为1
            #2. b给到a a=1
            #3. b=a+b  a=b
            a, b = b,a+b
            i+=1
fibonacci()