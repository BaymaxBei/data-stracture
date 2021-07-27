

'''
1. 打印字符串的所有子序列
'''

def substrlist(string, index, path, res):
    if index==len(string):
        res.append(path)
        return
    substrlist(string, index+1, path, res)
    substrlist(string, index+1, path+string[index], res)

def getsublist(string):
    res = []
    substrlist(string, 0, '', res)
    return res

'''
3. 打印字符串的所有全排列，字符串长度为n
'''
def permutation(str_list, index, path, res):
    if index==len(str_list):
        res.append(path)
        return
    for i in range(index, len(str_list)):
        str_list[index], str_list[i] = str_list[i], str_list[index]
        permutation(str_list, index+1, path+str_list[index], res)
        str_list[index], str_list[i] = str_list[i], str_list[index]

def get_permutation(string):
    str_list = list(string)
    res = []
    permutation(str_list, 0, '', res)
    return res

'''
4. 打印字符串的所有不重复全排列
    - 4.1 用set存储结果
    - 4.2 对于每个位置，若已经出现过某个字符，则弃掉该分支
'''
def permutation_unrepeat(str_list, index, path, res):
    if index==len(str_list):
        res.append(path)
        return
    tmp_set = set()
    for i in range(index, len(str_list)):
        if str_list[i] in tmp_set:
            return
        else:
            tmp_set.add(str_list[i])
            str_list[index], str_list[i] = str_list[i], str_list[index]
            permutation_unrepeat(str_list, index+1, path+str_list[index], res)
            str_list[index], str_list[i] = str_list[i], str_list[index]

def get_premutation_unrepeat(string):
    str_list = list(string)
    res = []
    permutation_unrepeat(str_list, 0, '', res)
    return res


if __name__ == '__main__':
    string = 'abaa'
    print(getsublist(string))
    print(get_permutation(string))
    print(get_premutation_unrepeat(string))
