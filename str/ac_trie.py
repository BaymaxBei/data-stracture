from typing import List
import time
import re
# import ahocorasick

class TrieNode:
    def __init__(self, node) -> None:
        '''
        初始化时，指定父节点
        '''
        self.is_root = False
        self.father = node
        self.word_len = []
        self.fail = None
        self.next = {}
        

class AcTrie:
    def __init__(self) -> None:
        # 根节点比较特殊，没有父节点,fail指针为自身
        self.trie = TrieNode(None)
        self.trie.is_root = True
        self.trie.fail = self.trie


    def add_word(self, word) -> None:
        node = self.trie
        for w in word:
            node = node.next.setdefault(w, TrieNode(node))
        node.word_len.append(len(word))

    def make(self) -> None:
        # 采用BFS遍历节点构建fail指针
        # 构建队列，每一层遍历结束才进行下一层遍历
        node_queue = []
        node_queue.append(self.trie)
        word_queue =[0]
        while node_queue:
            father = node_queue.pop(0)
            _tmp_word = word_queue.pop(0)
            for w, node in father.next.items():
                # 构建fail指针, 根节点的fail指针为自身，第一层的fail指针为root节点
                # 其他层的构建方式：若父节点不是根节点且其fail指针节点包含子节点w，
                #           则fail指针->父节点的fail指针节点的w子节点, 
                #           否则继续回溯父节点的fail指针的fail指针，直到fail指针指向根节点
                if father.is_root:
                    node.fail = father
                else:
                    pre_node = father
                    while not pre_node.is_root and w not in pre_node.fail.next:
                        pre_node = pre_node.fail
                    if w in pre_node.fail.next:
                        node.fail = pre_node.fail.next[w]
                        node.word_len.extend(node.fail.word_len)
                    else:
                        node.fail = self.trie
                node_queue.append(node)
                word_queue.append(w)


    def search(self, string) -> List:
        # 查找trie树，匹配字符串string
        node = self.trie
        res = []
        i = 0
        for i in range(len(string)):
            s = string[i]
            for k, cur_node in node.next.items():
                if k==s:
                    if cur_node.word_len:
                        for wlen in cur_node.word_len:
                            res.append([i-wlen+1, i+1, string[i-wlen+1:i+1]])
                    node = cur_node
                    break
            else:
                while s not in node.next and not node.is_root:
                    node = node.fail
                if s in node.next:
                    node = node.next[s]
        return res

# 目标：搞清楚什么时候next(i)=i+1,什么时候next(i)=i
# 起始，遍历root子节点，若失配，则next(i)=i+1，若再失配，则next(i)=i+1
#                    若匹配，则node下移，next(i)=i+1，
#                            若失配，则next(i)=i，
#                                 若失配，且上一节点为root，则next(i)=i+1
#                            若匹配，则next(i)=i+1
# 总结：若匹配， next(i)=i+1
#      若失配，若上一节点是root节点，则next(i)=i+1，否则next(i)=i

if __name__ == '__main__':
    words = ['she', 'hers', 'his', 'he', 'hi', 'hih', 'bg']
    string = 'abgvhihisbcsrshers'
#     words = ['break', '循环', '没', '语句', '公司', '']
#     string = 'break语句用来终止循环语句,即循环条件没有False条件或者序列还没被完全递归完,也会停止执行循'
#     words = ['嘉兴银行', '嘉兴城市', '嘉兴市嘉实金融控股']
#     string = '''
#     嘉兴银行因年报信息披露不完整等三项案由拿到今年首张罚单。
# 　　近日，银保监会公示了一张嘉兴银行的罚单，嘉兴银行因“关联交易未按要求进行审批；绩效考评指标类型和权重不符合监管规定；年报信息披露不完整”三项案由被嘉兴银保监局处以85万元罚款。这是嘉兴银行今年的第一张罚单。
# 　　根据嘉兴银行2020年年报显示，该行去年增收不增利。截至去年年末，嘉兴银行实现营业收入25.46亿元，同比增长7.26%，但净利润为6.45亿元，同比降低了4.36%。成本收入比为38.75%，比2019年末上升了6.82个百分点。该行去年年末总资产破千亿，达1046.73亿元，同比增长27.13%；总负债989.41亿元，同比增长28.44%。
# 　　在资产质量方面，该行不良贷款率为0.97%，同比下降0.15个百分点。从资本充足率指标来看，该行去年年末资本充足率为13.37%，比上一年度上升了0.56个百分点，但其核心一级资本充足率却降低了1.56个百分点，为8.57%，2019年末则为10.13%。
# 　　银保监会数据显示，2020年末，商业银行（不含外国银行分行）核心一级资本充足率为10.72%，一级资本充足率为12.04%，资本充足率为14.7%。嘉兴银行核心一级资本充足率远低于平均水平。
# 　　官网资料显示，嘉兴银行成立于1997年12月22日，原名嘉兴城市合作银行，是以嘉兴市原3家城市信用合作社和6家农村信用合作社为基础，由嘉兴市政府发起成立的全市首家具有法人资格的地方性股份制商业银行。1998年6月更名为嘉兴市商业银行，2009年12月更名为嘉兴银行。目前，嘉兴银行注册资本14.21亿元，下辖分支机构78家。
# 　　截至去年年末，该行前三大股东为嘉兴市嘉实金融控股有限公司、嘉兴市城市投资发展集团有限公司、嘉兴市现代服务业发展投资集团有限公司，均占股9.85%
#     '''
    ac_trie = AcTrie()
    for word in words:
        ac_trie.add_word(word)
    ac_trie.make()
    print(ac_trie)
    print(ac_trie.search(string))

    # time_ac_start = time.time()
    # for i in range(1000):
    #     ac_trie.search(string)
    # time_ac_end = time.time()

    # time_re_start = time.time()
    # for i in range(1000):
    #     # re.findall('|'.join(words), string)
    #     for w in words:
    #         re.findall(w, string)
    # time_re_end = time.time()
    # for w in words:
    #     print(re.findall(w, string))

    # ac_py = ahocorasick.Automaton()
    # for w in words:
    #     ac_py.add_word(w, (w))
    # ac_py.make_automaton()
    # time_ac_py_start = time.time()
    # for i in range(1000):
    #     for ind, (w) in ac_py.iter(string):
    #         pass
    # time_ac_py_end = time.time()


    # print('time ac: {}'.format(time_ac_end-time_ac_start))
    # print('time re: {}'.format(time_re_end-time_re_start))
    # print('time ac_py: {}'.format(time_ac_py_end-time_ac_py_start))

    # print(re.findall('a|ab|bc', 'abc'))
    # print(re.findall('招商银行|招商|招商银行股份', '招商银行股份'))
