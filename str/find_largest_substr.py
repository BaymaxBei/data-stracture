


'''
找到字符串中的最大不重复子串，返回长度
'''

def find_longest_unrepeat_substr(string):
    max_len = 0
    start_index = 0
    num_dict = {}
    index_dict = {}
    for i, s in enumerate(string):
        s_num = num_dict.get(s, 0)
        if s_num>0:
            s_index = index_dict[s]
            for j in range(start_index, s_index):
                num_dict[string[j]] = 0
            max_len = max(max_len, i-start_index)
            start_index = s_index + 1
            index_dict[s] = i
        else:
            num_dict[s] = 1
            index_dict[s] = i
    max_len = max(max_len, i-start_index+1)
    return max_len

if __name__ == '__main__':
    string = 'abccaddefagr'
    print(find_longest_unrepeat_substr(string))
