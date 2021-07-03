from binary_search_tree import Node, generate_random_BST, DLR, LDR, LRD, is_same_arr

def morris_in(head):
    '''
    # Morris遍历
    '''
    res = []
    while head is not None:
        if head.left is None:
            # 若左节点为空，则直接跳到右节点
            res.append(head.value)
            head = head.right
        else:
            # 否则找到左节点的最右子节点
            most_right = head.left
            while most_right.right is not None and most_right.right!=head:
                most_right = most_right.right
            if most_right.right is None: # 第一次找到最右子节点，说明第一次达到当前节点
                most_right.right = head # 将最后子节点的右节点指向当前节点，用于下一次判断
                res.append(head.value)
                head = head.left
            else: # 第二次找到最右子节点，说明第二次到达当前节点
                res.append(head.value)
                most_right.right = None # 重置最右子节点的右节点为空
                head = head.right
    return res

    
def morris_DLR(head):
    '''
    Morris遍历，前序遍历打印
    '''
    res = []
    while head is not None:
        if head.left is None:
            res.append(head.value)
            head = head.right
        else:
            most_right = head.left
            while most_right.right is not None and most_right.right!=head:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = head
                res.append(head.value)
                head = head.left
            else:
                most_right.right = None
                head = head.right
    return res

def morris_LDR(head):
    '''
    Morris遍历，中序遍历打印
    '''
    res = []
    while head is not None:
        if head.left is None:
            res.append(head.value)
            head = head.right
        else:
            most_right = head.left
            while most_right.right is not None and most_right.right!=head:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = head
                head = head.left
            else:
                res.append(head.value)
                most_right.right = None
                head = head.right
    return res

if __name__ == '__main__':
    bst = generate_random_BST(1, 100, 1, 4)

    bst_dlr = []
    DLR(bst, bst_dlr)
    print(bst_dlr)

    bst_ldr = []
    LDR(bst, bst_ldr)
    print(bst_ldr)

    bst_lrd = []
    LRD(bst, bst_lrd)
    print(bst_lrd)

    print(morris_in(bst))

    print(is_same_arr(bst_dlr, morris_DLR(bst)))
    print(is_same_arr(bst_ldr, morris_LDR(bst)))
    print('ok')