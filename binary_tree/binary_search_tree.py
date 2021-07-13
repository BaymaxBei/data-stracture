from math import floor
import random


class Node:
    '''
    节点
    '''
    def __init__(self, value, index=0) -> None:
        self.value = value
        self.index = index
        self.left = None
        self.right = None


def generate_random_BST(min, max, level, n):
    '''
    # 随机生成二叉搜索树
    最小值为min，最大值为max，最大高度为n
    '''
    if min>max or level>n:
        return None
    value = random.randint(min, max)
    head = Node(value)
    head.left = generate_random_BST(min, value-1, level+1, n)
    head.right = generate_random_BST(value+1, max, level+1, n)
    return head

def generate_BST_from_arr(arr):
    head = Node(arr[0], 0)
    for i, v in enumerate(arr[1:]):
        node = head
        while (node.left and v<node.value) or (node.right and v>=node.value):
            if v<node.value:
                node = node.left
            else:
                node = node.right
        if v<node.value: # v小于node且左节点为空
            node.left = Node(v, i)
        else: # v大于node且右节点为空
            node.right = Node(v, i)
    return head



def LDR(head, res):
    '''
    # 中序遍历二叉树
    '''
    if head.left:
        LDR(head.left, res)
    res.append(head.value)
    if head.right:
        LDR(head.right, res)

def LRD(head, res):
    '''
    # 后续遍历二叉树
    '''
    if head.left:
        LRD(head.left, res)
    if head.right:
        LRD(head.right, res)
    res.append(head.value)

def DLR(head, res):
    '''
    # 前序遍历二叉树
    '''
    res.append(head.value)
    if head.left:
        DLR(head.left, res)
    if head.right:
        DLR(head.right, res)

def DLR_stack(head):
    '''
    前序遍历二叉树，非递归，用栈
    '''
    node = head
    stack = []
    res = []
    while node is not None or len(stack)!=0:
        if node is not None:
            stack.append(node)
            res.append(node.value)
            node = node.left
        else:
            node = stack.pop(-1)
            node = node.right
    return res

def LDR_stack(head):
    '''
    中序遍历二叉树，非递归，用栈
    '''
    node = head
    stack = []
    res = []
    while node is not None or len(stack)!=0:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop(-1)
            res.append(node.value)
            node = node.right
    return res

def is_same_arr(arr1, arr2):
    '''
    # 判断两个数组是否相同
    '''
    if len(arr1)!=len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            return False
    return True


def generate_BST_by_LRD1(arr, l, r):
    '''
    # 根据二叉搜索树的后序遍历结果重构二叉搜索树
    遍历寻找左右子树的分界点
    '''
    if l>r:
        return None
    node = Node(arr[r])
    # if l==r:
    #     return node
    flag = l - 1
    # 找到左右子树的分界点
    for i in range(l, r):
        if arr[i]<arr[r]:
            flag+=1
        else:
            break
    node.left = generate_BST_by_LRD1(arr, l, flag)
    node.right = generate_BST_by_LRD1(arr, flag+1, r-1)
    return node

def find_flag(arr, l, r, value):
    '''
    # 查找左右子树的分界点，小于value的最右索引
    二分法，递归
    '''
    if l==r and arr[l]<value:
        return l
    if l==r and arr[l]>value:
        return l-1
    flag = l + floor((r-l)/2)
    if arr[flag]<value:
        return find_flag(arr, flag+1, r, value)
    else:
        return find_flag(arr, l, flag-1, value)

def find_flag2(arr, l, r, value):
    '''
    查找左右子树的分界点，小于value的最右索引
    # 二分法，非递归
    '''
    flag = l-1
    while l<=r:  # 当l=r时，判断结束
        median = l + floor((r-l)/2)
        if arr[median]<value:
            # 当选中值小于value时，移动flag到此处
            flag = median
            l = median+1
        else:
            r = median-1 
    return flag

def generate_BST_by_LRD2(arr, l, r):
    '''
    根据二叉搜索树的后序遍历结果重构二叉搜索树
    利用二分法寻找左右子树的分界点
    '''
    if l>r:
        return None
    node = Node(arr[r])
    # if l==r:
    #     return node
    flag = find_flag2(arr, l, r-1, arr[r])
    node.left = generate_BST_by_LRD2(arr, l, flag)
    node.right = generate_BST_by_LRD2(arr, flag+1, r-1)
    return node


if __name__ == '__main__':
    # arr = [3,4,5,11,16,15,10]
    # bst = generate_BST_by_LRD2(arr, 0, len(arr)-1)
    # print('End.')
    
    for i in range(10):
        
        bst = generate_random_BST(1, 100, 1, 5)
        bst_ldr = []
        LDR(bst, bst_ldr)
        ldr2 = LDR_stack(bst)
        if not is_same_arr(bst_ldr, ldr2):
            print('no')
            print(bst_ldr)

        # bst_generate = generate_BST_by_LRD2(bst_lrd, 0, len(bst_lrd)-1)
        # bst_generate_lrd = []
        # LRD(bst_generate, bst_generate_lrd)

        # if not is_same_arr(bst_lrd, bst_generate_lrd):
        #     print('oh no.')
        #     print(bst_lrd)
        # print(bst_lrd)
        # print('ok')
    print('ok.')

    # for i in range(10000):
        
    #     bst = generate_random_BST(1, 100, 1, 5)
    #     bst_lrd = []
    #     LRD(bst, bst_lrd)

    #     bst_generate = generate_BST_by_LRD2(bst_lrd, 0, len(bst_lrd)-1)
    #     bst_generate_lrd = []
    #     LRD(bst_generate, bst_generate_lrd)

    #     if not is_same_arr(bst_lrd, bst_generate_lrd):
    #         print('oh no.')
    #         print(bst_lrd)
    #     # print(bst_lrd)
    #     # print('ok')
    # print('ok.')

    # arr = [8]
    # arr.extend(list(range(10)))
    # arr = [0]*10
    # arr = [random.randrange(0, 10, 1) for i in arr]
    # print(arr)
    # bst = generate_BST_from_arr(arr)
    # print(bst)
