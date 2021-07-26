'''
返回两个有序数组的中位数
'''

def medium_of(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1)%2==0:
        return (nums1[int(len(nums1)/2)-1]+nums1[int(len(nums1)/2)])/2
    else:
        return nums1[int(len(nums1)/2)] 


class Solution:
    '''
    leetcode solution by else.
    '''
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        m, nMod = divmod(n, 2)

        if n1 == 0 or n2 == 0:
            nums = nums1 + nums2
            if nMod == 0:
                return sum(nums[m-1:m+1]) / 2
            else:
                return nums[m]
        
        p1 = 0
        p2 = 0
        k = 0
        selectedNums = []
        while True:
            if p2 >= n2 or (p1 < n1 and nums1[p1] <= nums2[p2]):
                num = nums1[p1]
                p1 += 1
            else:
                num = nums2[p2]
                p2 += 1
            k += 1
            if nMod == 0 and k == m:
                selectedNums.append(num)
            if k == m + 1:
                selectedNums.append(num)
                return sum(selectedNums) / (2 - nMod)



if __name__ == '__main__':
    arr1 = [1,3,5]
    arr2 = [2,4]
    print(medium_of(arr1, arr2))
    Solution().findMedianSortedArrays(arr1, arr2)