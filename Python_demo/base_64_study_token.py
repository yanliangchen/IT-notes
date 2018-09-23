# -*- coding: utf-8 -*-

__author__ = 'yanliangchen'
import base64

'''
参见 : https://blog.csdn.net/wo541075754/article/details/81734770
一 . Base64的了解 
1 . Base-64编码保证了二进制数据的安全
2 . 大多数编码都是由字符串转化成二进制的过程，而Base64的编码则是从二进制转换为字符串。与常规恰恰相反，
3 . Base64编码主要用在传输、存储、表示二进制领域，不能算得上加密，只是无法直接看到明文。也可以通过打乱Base64编码来进行加密。
4 . 上面我们已经看到了Base64就是用6位（2的6次幂就是64）表示字符，因此成为Base64。同理，Base32就是用5位，Base16就是用4位。

二 .Base64的原理
第一步，将待转换的字符串每三个字节分为一组，每个字节占8bit，那么共有24个二进制位。
第二步，将上面的24个二进制位每6个一组，共分为4组。
第三步，在每组前面添加两个0，每组由6个变为8个二进制位，总共32个二进制位，即四个字节。
第四步，根据Base64编码对照表（见下图）获得对应的值。
0　A　　17　R　　　34　i　　　51　z

1　B　　18　S　　　35　j　　　52　0

2　C　　19　T　　　36　k　　　53　1

3　D　　20　U　　　37　l　　　54　2

4　E　　21　V　　　38　m　　　55　3
....

三 .应用
    目前Base64已经成为网络上常见的传输8Bit字节代码的编码方式之一。在做支付系统时，系统之间的报文交互都需要使用Base64对明文进行转码，
    然后再进行签名或加密，之后再进行（或再次Base64）传输。那么，Base64到底起到什么作用呢？

    在参数传输的过程中经常遇到的一种情况：使用全英文的没问题，但一旦涉及到中文就会出现乱码情况。
    与此类似，网络上传输的字符并不全是可打印的字符，比如二进制文件、图片等。Base64的出现就是为了解决此问题，
    它是基于64个可打印的字符来表示二进制的数据的一种方法。

    电子邮件刚问世的时候，只能传输英文，但后来随着用户的增加，中文、日文等文字的用户也有需求，但这些字符并不能被服务器或网关有效处理，
    因此Base64就登场了。随之，Base64在URL、Cookie、网页传输少量二进制文件中也有相应的使用。


'''
import json


# 这里给做成token
class Token(object):
    '''
    token : base64编码
    '''

    def __init__(self):
        # 先初始一段字符串
        self._key = '123qweasdzxc'

    # base64加密
    def sign(self, data):
        data += '.%s' % self._key
        print data
        return base64.b64encode(data)

    # base64解密
    def unsign(self, data):
        return base64.b64decode(data)


if __name__ == '__main__':
    token = Token()
    # 测试字符串
    a = token.sign('1234')
    b = token.unsign(a)
    print a, b
    # 测试字典  sort_keys参数对键的值进行排序
    test_dict_str = json.dumps({'z': 56, 'm': 12, 'p': 34}, sort_keys=True)
    a = token.sign(test_dict_str)
    b = token.unsign(a)
    print a, b