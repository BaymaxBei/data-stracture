

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

'''
5. 数字组成的字符串映射为字母，1~26对应A~Z，求所有可能映射结果或结果个数
'''
def num2letter(str_list, index, res, path):
    if index==len(str_list):
        res.append(path)
        return
    if str_list[index]=='0':
        return
    elif str_list[index]=='1':
        num2letter(str_list, index+1, res, path+chr(int(str_list[index])+64))
        if index+1<len(str_list):
            num2letter(str_list, index+2, res, path+chr(int(str_list[index]+str_list[index+1])+64))
    elif str_list[index]=='2':
        num2letter(str_list, index+1, res, path+chr(int(str_list[index])+64))
        if index+1<len(str_list) and int(str_list[index+1])<7:
            num2letter(str_list, index+2, res, path+chr(int(str_list[index]+str_list[index+1])+64))
    else:
        num2letter(str_list, index+1, res, path+chr(int(str_list[index])+64))

def get_num2letter(string):
    res = []
    num2letter(list(string), 0, res, '')
    return res

# 返回结果数量
def num2letter_count(str_list, index, count):
    if index==len(str_list):
        return 1
    if str_list[index]=='0':
        return 0
    if str_list[index]=='1':
        c = num2letter_count(str_list, index+1, count)
        if index+1<len(str_list):
            c += num2letter_count(str_list, index+2, count)
        return count + c
    if str_list[index]=='2':
        c = num2letter_count(str_list, index+1, count)
        if index+1<len(str_list) and int(str_list[index+1])<7:
            c += num2letter_count(str_list, index+2, count)
        return count + c
    return count + num2letter_count(str_list, index+1, count)

def get_num2letter_count(strint):
    return num2letter_count(list(string), 0, 0)


'''
6. 背包具有价值和重量，如何选择背包使得满足重量不超的情况下价值最大
'''
def most_value_of_bags(bags_list, index, cur_weight, max_weight, cur_value, max_value):
    # 传入当前选择的总价值、总重量和全局总重量阈值，每次更新全局最大价值
    if index==len(bags_list):
        return max(max_value, cur_value)
    max_value = most_value_of_bags(bags_list, index+1, cur_weight, max_weight, cur_value, max_value)
    cur_weight = bags_list[index].weight + cur_weight
    cur_value = bags_list[index].value + cur_value
    if cur_weight<=max_weight:
        max_value = most_value_of_bags(bags_list, index+1, cur_weight, max_weight, cur_value, max_value)
    return max_value

def get_most_value_of_bags(bags_list, max_weight):
    return most_value_of_bags(bags_list, 0, 0, max_weight, 0, -float('inf'))

def most_value_of_bags_2(bags_list, index, cur_weight, max_weight):
    # 传入当前选择的总重量和全局总重量阈值，返回当前节点及后面的最大价值
    if index==len(bags_list):
        return 0
    v1 = most_value_of_bags_2(bags_list, index+1, cur_weight, max_weight)
    cur_weight = cur_weight + bags_list[index].weight
    if cur_weight<=max_weight:
        v2 = bags_list[index].value + most_value_of_bags_2(bags_list, index+1, cur_weight, max_weight)
        return max(v1, v2)
    else:
        return v1
    

def get_most_value_of_bags_2(bags_list, max_weight):
    return most_value_of_bags_2(bags_list, 0, 0, max_weight)

def get_most_value_of_bags_test():
    class Bag:
        def __init__(self, weight, value) -> None:
            self.weight = weight
            self.value = value
    weights = [2,3,2,4,5]
    values = [19,2,1,0,2]
    bags_list = [Bag(i, j) for i, j in zip(weights, values)]
    print(get_most_value_of_bags(bags_list, 3))
    print(get_most_value_of_bags_2(bags_list, 3))


'''
N皇后问题
'''

if __name__ == '__main__':
    # string = 'abaa'
    # print(getsublist(string))
    # print(get_permutation(string))
    # print(get_premutation_unrepeat(string))

    # string = '11218'
    # print(get_num2letter(string))
    # print(get_num2letter_count(string))

    get_most_value_of_bags_test()

