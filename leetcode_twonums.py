class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.bst_head = None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.build_large_search_tree(nums, target)
        for i, v in enumerate(nums):
            if v<target:
                res = self.search_bst(target-v)
                if res:
                    return [i,res]


    def build_large_search_tree(self, nums: List[int],target):
        for i, v in enumerate(nums):
            if v>=target:
                if self.bst_head is None:
                    self.bst_head = Node(v, i)
                else:
                    node = self.bst_head
                    while (node.left and v<node.value) or (node.right and v>=node.value):
                        if v<node.value:
                            node = node.left
                        else:
                            node = node.right
                    if v<node.value: # v小于node且左节点为空
                        node.left = Node(v, i)
                    else: # v大于node且右节点为空
                        node.right = Node(v, i)
    
    def search_bst(self, num):
        if self.bst_head:
            node = self.bst_head
            while (node.left and num<node.value) or (node.right and num>node.value):
                if num<node.value:
                    node = node.left
                else:
                    node = node.right
            if num==node.value:
                return node.index
            return False
        return False
            
            
if __name__ == '__main__':
    pass