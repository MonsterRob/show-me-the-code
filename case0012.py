import re
from case0011 import generatepat, getflag

def ignoreword(s, pattern):
    return re.sub(pattern, lambda mo: mo.group(0).__len__()*'*', s)

if __name__ == '__main__':
    path = 'resource/filtered_words.txt'
    pattern = '(' + generatepat(path) + ')'
    flag = 0
    while flag == 0:
        s = input('Input: ')
        result = ignoreword(s, pattern)
        print(result)
        flag = getflag()
    print("Bye...")