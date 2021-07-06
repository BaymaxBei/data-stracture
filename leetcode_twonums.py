import random


class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.bst_head = None

    def twoSum1(self, nums, target: int):
        self.build_large_search_tree(nums, target)
        for i, v in enumerate(nums):
            res = self.search_bst(target-v)
            if res is not None and i!=res:
                return [i,res]

    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            sub = target - v
            if sub in d:
                return [i, d[sub]]
            d[v] = i
        

    def build_large_search_tree(self, nums,target):
        start = random.randrange(0, len(nums))
        self.bst_head = Node(nums[start], start)
        for i, v in enumerate(nums):
            if i!=start:
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
            return None
        return None
            
            
if __name__ == '__main__':
    arr = [3,3]
    target = 6
    print(Solution().twoSum(arr, target))
