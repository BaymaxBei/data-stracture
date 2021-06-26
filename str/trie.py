


class Trie(object):
    '''
    trie树
    '''
    def __init__(self) -> None:
        self.trie = {}

    def insert(self, word):
        tmp = self.trie
        for w in word:
            if w not in tmp:
                tmp[w] = {}
            tmp = tmp[w]
        tmp['is_word'] = True

    def search(self, word):
        tmp = self.trie
        for w in word:
            if w in tmp:
                tmp = tmp[w]
            else:
                return False
        return tmp.get('is_word', False)

    def startsWith(self, prefix):
        tmp = self.trie
        for p in prefix:
            if p in tmp:
                tmp = tmp[p]
            else:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('abc')
    print('search: {}: {}'.format('abc', trie.search('abc')))
    print('search: {}: {}'.format('ab', trie.search('ab')))
    print('startsWith: {}: {}'.format('ab', trie.startsWith('ab')))
    print(trie.trie)


