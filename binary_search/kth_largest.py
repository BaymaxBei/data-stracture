import random
import time
'''
查找数组中第k大（小）的数
'''

# LeetCode 某一范例
class Solution(object):
    def findKthLargest(self, nums, k):
        H = SmallHeap()
        H.CreateHeap(nums[:k])
        temp = H.heap
        for x in nums[k:]:
            if x > temp[1]:
                temp[1] = x
                H.HeapAdjust(temp,1,k)
        return temp[1]

class SmallHeap:
    def __init__(self):
        self.heap = []
    def HeapAdjust(self, arr, k, l):
        i = 2 * k
        while i <= l:
            if i < l and arr[i] > arr[i+1]:
                i += 1
            if arr[k] <= arr[i]: break
            else:
                arr[k], arr[i] = arr[i], arr[k]
                k = i
                i *= 2

    def CreateHeap(self, arr):
        m = int(len(arr) / 2)
        arr.insert(0,0)
        l = len(arr) - 1
        while m >= 1:
            self.HeapAdjust(arr,m,l)
            m -= 1
        self.heap = arr
        return arr[1:]

    def HeapPop(self):
        heaptop = self.heap.pop(1)
        self.heap.insert(1,self.heap.pop())
        l = len(self.heap) - 1
        self.HeapAdjust(self.heap, 1, l)
        return heaptop

def partition(arr, l, r, value):
    flag = l
    l = l -1 
    r = r + 1
    while flag!=r:
        if arr[flag]<value:
            l += 1
            arr[l], arr[flag] = arr[flag], arr[l]
            flag += 1
        elif arr[flag]>value:
            r -= 1
            arr[r], arr[flag] = arr[flag], arr[r]
        else:
            flag += 1
    return [l+1, r-1]

def kth_largest(arr, k):
    '''
    二分法
    '''
    pos = len(arr) - k
    l = 0
    r = len(arr)-1
    while l<r:
        rand = random.randrange(l, r)
        rand_value = arr[rand]
        less, larger = partition(arr, l, r, rand_value)
        if less<=pos<=larger:
            return rand_value
        elif pos<less:
            r = less
        else:
            l = larger
    return arr[l]

def kth_largest_base(arr, k):
    '''
    对数器，从小到大排序后取第 len(arr)-k 个数
    '''
    arr.sort(reverse=True)
    return arr[k-1]


def kth_smallest(arr, k):
    '''
    二分法
    '''
    pos = k-1
    l = 0
    r = len(arr)-1
    while l<r:
        rand = random.randrange(l, r)
        rand_value = arr[rand]
        less, larger = partition(arr, l, r, rand_value)
        if less<=pos<=larger:
            return rand_value
        elif pos<less:
            r = less
        else:
            l = larger
    return arr[l]

def kth_smallest_base(arr, k):
    '''
    对数器，从小到大排序后取第 len(arr)-k 个数
    '''
    arr.sort()
    return arr[k-1]


def is_same(num1, num2):
    if num1==num2:
        return True
    else:
        return False

def generate_random_arr(max_num, dim):
    arr = [random.randrange(0, max_num) for i in range(dim)]
    return arr

if __name__ == '__main__':
    ##### one test
    # arr = generate_random_arr(50, 10)
    # print(arr)
    # print(partition(arr, 0, len(arr)-1, arr[5]))
    # print(kth_largest_base(arr, 3))
    # print(kth_largest(arr, 3))

    ###### kth largest test
    # for i in range(100):
    #     arr = generate_random_arr(1000, 50)
    #     k = 20
    #     if not kth_largest_base(arr, k)==kth_largest(arr, k):
    #         print('no')
    #         print(arr, k)

    ###### kth smallest test
    for i in range(100):
        arr = generate_random_arr(1000, 50)
        k = 20
        if not kth_smallest_base(arr, k)==kth_smallest(arr, k):
            print('no')
            print(arr, k)

    ###### time compare
    arrs = []
    for i in range(10000):
        arr = generate_random_arr(1000, 5000)
        arrs.append(arr)
        k = 200

    t0 = time.time()
    for arr in arrs:
        kth_largest_base(arr, k)
    t1 = time.time()
    print('base time: {}'.format(t1-t0))

    for arr in arrs:
        kth_largest(arr, k)
    t2 = time.time()
    print('binary time: {}'.format(t2-t1))


