class Solution:
    '''
    
    '''
    def max_sub_str_unrepeat(self, string):
        '''
        滑动窗口，若大于1，则初始化开始位置
        '''
        max_len = 0
        start_pos = 0
        max_sub_str = ''
        symbol_num = {}
        symbol_index = {}
        
        for i,s in enumerate(string):
            s_num = symbol_num.get(s, 0)
            if s_num==0:
                symbol_num[s] = 1
                symbol_index[s] = i
            else:
                cur_len = i - start_pos
                if cur_len>max_len:
                    max_sub_str = string[start_pos: i]
                max_len = max(max_len, cur_len)
                s_index = symbol_index[s]
                for pre_s_index in range(start_pos, s_index+1):
                    symbol_num[string[pre_s_index]] = 0
                start_pos = s_index + 1

        return max_sub_str


if __name__  ==  '__main__':
    string='adsfabfda'
    print(Solution().max_sub_str_unrepeat(string))