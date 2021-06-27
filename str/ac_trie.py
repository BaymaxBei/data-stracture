from typing import List


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
        # 根节点比较特殊，没有父节点、fail指针
        self.trie = TrieNode(None)
        self.trie.is_root = True
        self.trie.fail = self.trie


    def add_word(self, word) -> None:
        father = self.trie
        for w in word:
            if w in father.next:
                node = father.next[w]
            else:
                node = TrieNode(father)
                father.next[w] = node
                # 构建fail指针, 根节点的fail指针为自身，其余为其他TrieNode
                # 构建方式：若父节点不是根节点且其fail指针节点包含子节点w，
                #           则fail指针指向父节点的fail指针节点的w子节点, 
                #           否则fail指针指向根节点
                if  not father.is_root and w in father.fail.next:
                    node.fail = father.fail.next[w]
                    node.word_len.extend(node.fail.word_len)
                else:
                    node.fail = self.trie
            father = node
        father.word_len.append(len(word))

    def search(self, string) -> List:
        # 查找trie树，匹配字符串string
        node = self.trie
        res = []
        i = 0
        while i<len(string):
            pre = node
            for w in node.next:
                if w==string[i]:
                    node = node.next[w]
                    if node.word_len:
                        for l in node.word_len:
                            res_i = [i-l+1, i+1, string[i-l+1: i+1]]
                            res.append(res_i)
                    if not node.next:
                        node = node.fail
                    i += 1
                    break
            else:
                if pre.is_root:
                    i += 1
                node = node.fail
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
    words = ['he', 'hers', 'his', 'she']
    string = 'abgvhihisbcsrhers'
    words = ['break', '循环', '没', '语句']
    string = 'break语句用来终止循环语句,即循环条件没有False条件或者序列还没被完全递归完,也会停止执行循'
    ac_trie = AcTrie()
    for word in words:
        ac_trie.add_word(word)
    print(ac_trie)
    print(ac_trie.search(string))
