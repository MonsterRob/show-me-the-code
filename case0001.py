import random
import string

def generatecode(num, prefixnum, postnum):
    """
    生成唯一激活码，序列号（prefixnum位）+无序字符串（postnum位）
    :param num: 要生成的个数
    :param prefixnum: 前缀位数
    :param postnum: 后缀位数
    :return: 含激活码的集合
    """
    l =[]
    for i in range(num):
        prefix = '{:0{prefixnum}X}'.format(i+1, prefixnum=prefixnum)
        post = ''
        for j in range(postnum):
            post += random.choice(string.ascii_letters+string.digits)
        l.append(prefix+post)
    return l

if __name__ == '__main__':
    l = generatecode(200, 6, 10)
    for s in l:
        print(s)