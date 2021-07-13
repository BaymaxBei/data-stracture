import random

class Solution:

    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            sub = target - v
            if sub in d:
                return [i, d[sub]]
            d[v] = i
           
            
if __name__ == '__main__':
    arr = [3,3]
    target = 6
    print(Solution().twoSum(arr, target))
