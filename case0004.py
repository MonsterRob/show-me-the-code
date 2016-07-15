import re

def countNum(s):
    """
    :param s: 需要统计的文本
    :return: 返回文本中单词的个数
    """
    pattern = r"(\b\w+(\-\w+)*('s)?\b)"
    result = re.findall(pattern, s)
    return result.__len__()

if __name__ == '__main__':
    with open('resource/python-tutorial.txt') as f:
        print(countNum(f.read()))