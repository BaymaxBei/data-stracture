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


def generate_random_BST(min, max, level=1, n=3):
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

def level_traversal(head):
    res = []
    queue = []
    queue.append(head)
    while queue:
        node = queue.pop(0)
        res.append(node.value if node else node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res

def DLR_Series(head, res):
    '''
    前序遍历二叉树，序列化，空节点返回空
    '''
    res.append(head.value)
    if head.left:
        DLR_Series(head.left, res)
    elif head.right:
        res.append(None)
    if head.right:
        DLR_Series(head.right, res)
    elif head.left:
        res.append(None)

def DLR(head, res):
    '''
    # 前序遍历二叉树
    '''
    res.append(head.value)
    if head.left:
        DLR(head.left, res)
    if head.right:
        DLR(head.right, res)

def LDR_Series(head, res):
    '''
    中序遍历二叉树，序列化，空节点返回空
    '''
    if head.left:
        LDR_Series(head.left, res)
    elif head.right:
        res.append(None)
    res.append(head.value)
    if head.right:
        LDR_Series(head.right, res)
    elif head.left:
        res.append(None)

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

def LDR_stack_2(head):
    '''
    中序遍历二叉树，非递归，用栈
    '''
    node = head
    stack = []
    res = []
    stack.append(node)
    while stack:
        if node.left is not None:
            node = node.left
            stack.append(node)
        elif node.right is not None:
            node = stack.pop(-1)
            res.append(node.value)
            node = node.right
            stack.append(node)
        else:
            node = stack.pop(-1)
            res.append(node.value)
            while node.right is None and stack:
                node = stack.pop(-1)
                res.append(node.value)
            if node.right is not None:
                node = node.right
                stack.append(node)
    return res


def LDR_stack_3(head):
    '''
    中序遍历二叉树，非递归，用栈
    '''
    node = head
    stack = []
    res = []
    stack.append(node)
    while stack:
        if node.left is not None:
            node = node.left
            stack.append(node)
        else:
            node = stack.pop(-1)
            res.append(node.value)
            while node.right is None and stack:
                node = stack.pop(-1)
                res.append(node.value)
            if node.right is not None:
                node = node.right
                stack.append(node)
    return res

def LRD_stack(head):
    '''
    后序遍历二叉树，非递归，用栈
    '''
    res = []
    stack = []
    while head is not None or stack:
        if head is not None:
            stack.append(head)
            res.append(head.value)
            head = head.right
        else:
            head = stack.pop(-1)
            head = head.left
    res.reverse()
    return res

def LRD_stack_2(head):
    '''
    后序遍历二叉树，用栈和标记符
    '''
    res = []
    stack = []
    stack.append(head)
    cur_peek = None # 表示当前栈顶节点，
    last_pop = head # 这里的设置要以不影响逻辑判断为依据，不能设置为None
    while stack:
        cur_peek = stack[-1]
        if cur_peek.left is not None and last_pop != cur_peek.left and last_pop != cur_peek.right:
            stack.append(cur_peek.left)
        elif cur_peek.right is not None and last_pop != cur_peek.right:
            stack.append(cur_peek.right)
        else:
            last_pop = stack.pop(-1)
            res.append(last_pop.value)
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

def max_level_num(head):
    '''
    求二叉树的最长层的节点数
    '''
    if head is None:
        return 0
    queue = []
    node_level_dict = {}
    cur_level = 1
    cur_num = 1
    max_level_num = 1
    level_num = [1]
    node_level_dict[head] = 1
    queue.append(head)
    while queue:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
            node_level = node_level_dict[node] + 1
            node_level_dict[node.left] = node_level
            if node_level==cur_level:
                cur_num += 1
            else:
                cur_level = node_level
                max_level_num = max(cur_num, max_level_num)
                level_num.append(cur_num)
                cur_num = 1
        if node.right is not None:
            queue.append(node.right)
            node_level = node_level_dict[node] + 1
            node_level_dict[node.right] = node_level
            if node_level==cur_level:
                cur_num += 1
            else:
                cur_level = node_level
                max_level_num = max(cur_num, max_level_num)
                level_num.append(cur_num)
                cur_num = 1
    level_num.append(cur_num)
    return max(cur_num,max_level_num), level_num


def series_test():
    arr = [random.randint(1, 20) for i in range(9)]
    arr = [9, 10, 2, 13, 14, 17, 11, 6, 3]
    print(arr)
    bst = generate_BST_from_arr(arr)

    res = level_traversal(bst)
    print('层次遍历：{}'.format(res))

    bst_dlr_series = []
    DLR_Series(bst, bst_dlr_series)
    print('前序序列化：{}'.format(bst_dlr_series))

    bst_dlr = []
    DLR(bst, bst_dlr)
    print('前序遍历：{}'.format(bst_dlr))

    bst_ldr_series = []
    LDR_Series(bst, bst_ldr_series)
    print('中序序列化：{}'.format(bst_ldr_series))

    bst_ldr = []
    LDR(bst, bst_ldr)
    print('中序遍历：{}'.format(bst_ldr))

def traversal_test():
    arr = [9, 10, 2, 13, 14, 17, 11, 6, 3]
    print(arr)
    bst = generate_BST_from_arr(arr)

    bst_ldr_series = []
    LDR_Series(bst, bst_ldr_series)
    print('中序序列化：{}'.format(bst_ldr_series))

    bst_ldr = []
    LDR(bst, bst_ldr)
    print('中序遍历：{}'.format(bst_ldr))

    res = LDR_stack_2(bst)
    print('中序遍历，非递归2：{}'.format(res))

    res = LDR_stack_3(bst)
    print('中序遍历，非递归3：{}'.format(res))

def lrd_test():
    arr = [9, 10, 2, 13, 14, 17, 11, 6, 3]
    print(arr)
    bst = generate_BST_from_arr(arr)

    lrd = []
    LRD(bst, lrd)
    print('后序遍历：{}'.format(lrd))

    res = LRD_stack(bst)
    print('后序遍历，用栈：{}'.format(res))

    res = LRD_stack_2(bst)
    print('后序遍历，用栈2：{}'.format(res))

    error = 0
    for i in range(100):
        bst = generate_random_BST(1, 30)
        lrd = []
        LRD(bst, lrd)

        lrd_stack_2 = LRD_stack_2(bst)
        if not is_same_arr(lrd, lrd_stack_2):
            print('no')
            print(lrd)
            error += 1
    print('ok')
    print('error: {}'.format(error))

def max_level_num_test():
    # arr = [9, 10, 2, 13, 14, 17, 11, 6, 3]
    # print(arr)
    # bst = generate_BST_from_arr(arr)
    bst = generate_random_BST(1, 200, 1, 5)
    print(level_traversal(bst))
    print(max_level_num(bst))



if __name__ == '__main__':
    # series_test()

    # traversal_test()

    # lrd_test()

    max_level_num_test()

    # arr = [3,4,5,11,16,15,10]
    # bst = generate_BST_by_LRD2(arr, 0, len(arr)-1)
    # print('End.')
    
    # error = 0
    # for i in range(10):
        
    #     bst = generate_random_BST(1, 100, 1, 3)
    #     bst_ldr_series = []
    #     LDR_Series(bst, bst_ldr_series)
    #     bst_ldr = []
    #     LDR(bst, bst_ldr)
    #     print(bst_ldr_series)
    #     print(bst_ldr)
        # ldr2 = LDR_stack_2(bst)
        # if not is_same_arr(bst_ldr, ldr2):
        #     error += 1
        #     print('no')
        #     print(bst_ldr)
        #     print(ldr2)

        # bst_generate = generate_BST_by_LRD2(bst_lrd, 0, len(bst_lrd)-1)
        # bst_generate_lrd = []
        # LRD(bst_generate, bst_generate_lrd)

        # if not is_same_arr(bst_lrd, bst_generate_lrd):
        #     print('oh no.')
        #     print(bst_lrd)
        # print(bst_lrd)
        # print('ok')
    # print('ok.')
    # print('error: {}'.format(error))

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
