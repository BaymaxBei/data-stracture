import re

'''
KMP（Knuth, Morris, Pratt）算法：
单个模式串和字符串的匹配：判断模式串 P 是否在字符串 S 中出现

1. 遍历S，判断是否和P匹配
2. 若失配，根据失配数组（Next数组）将模式串向后移位继续匹配
3. 失配数组：若匹配在模式串P的第（i+1）个位置匹配失败，则从模式串P的第k个位置开始继续匹配，
    其中，k是模式子串P[0]~P[i]的最大相同前后缀的长度

Author: Bei Zhang.
'''

def generate_next(p):
    '''
    生成模式串P的next数组
    对于模式串P的位置i，P[0]~P[i]的最长公共前后缀长度k满足：
    i = 0, k = 0
    i = 1, k = 0
    i = 2..., 已知next[i-1]=k, 若P[i]=P[k], 则next[i]=k+1, 
                否则k=next[k], 继续判断if P[i]=P[k], 直到k=0
    '''
    next = [0, 0]
    k = 0
    i = 2
    while i<len(p):
        if p[i]==p[k]:
            k = k+1
            next.append(k)
            i += 1
        elif k:
            k = next[k-1]
        else:
            next.append(0)
            i += 1
    return next


def kmp(p, s):
    next = generate_next(p)
    plen = len(p)
    slen = len(s)
    # 从字符串p的起始点开始匹配
    i = 0
    # 遍历字符串s
    for j in range(slen):
        # 判断模式串p和字符串s是否匹配
        if p[i] == s[j]:
            i+=1
        else:
            i = next[i] + 1
        if i==plen:
            return (j-i, j)
    return False


if __name__ == '__main__':
    p = 'abcabdeabcabc'
    s = 'abcabdeabcabdabcabdeabcabcabcabdeabcabd'
    print(generate_next(p))
    print(kmp(p, s))