


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

def get_num2letter_count(string):
    return num2letter_count(list(string), 0, 0)


def num2letter_count_dp(string):
    ...

if __name__ == '__main__':
    # string = 'abaa'
    # print(getsublist(string))
    # print(get_permutation(string))
    # print(get_premutation_unrepeat(string))

    string = '11218'
    print(get_num2letter(string))
    print(get_num2letter_count(string))
