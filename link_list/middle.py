import random


class Node:
    '''
    单链表结点
    '''
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# 输入链表头结点，奇数长度返回中点，偶数长度返回上中点
class MidOrPremid:
    def solution(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def base(self, head):
        arr = []
        if head is None:
            return head
        while head:
            arr.append(head.value)
            head = head.next
        return arr[int((len(arr)-1)/2)]


# 输入链表头结点，奇数长度返回中点，偶数长度返回下中点
class MidOrPostMid:
    def solution(self, head):
        if head is None:
            return head
        if head.next is None:
            return head.value
        slow = head.next
        fast = head.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def base(self, head):
        if head is None:
            return head
        arr = []
        while head:
            arr.append(head.value)
            head = head.next
        return arr[int(len(arr)/2)]


# 输入链表头结点，奇数长度返回中点前一个，偶数长度返回上中点前一个
class PreMidOrPrePreMid:
    def solution(self, head):
        if head is None or head.next is None or head.next.next is None:
            return None
        slow = head
        fast = head.next.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def base(self, head):
        if head is None:
            return None
        arr = []
        while head:
            arr.append(head.value)
            head = head.next
        if len(arr)<=2:
            return None
        return arr[int((len(arr)-3)/2)]


# 输入链表头结点，奇数长度返回中点前一个，偶数长度返回下中点前一个

# 生成测试链表
class Test:
    def generate_linklist(self, n=10, m=10):
        if n==0:
            return None
        arr = [random.randrange(0, m) for i in range(n)]
        # print(arr)
        head = Node(arr[0])
        last = head
        for a in arr[1:]:
            node = Node(a)
            last.next = node
            last = node
        return head

if __name__ == '__main__':
    for i in range(1000):
        linklist = Test().generate_linklist(n=random.randrange(0, 10), m=100)
        # print(linklist)
        # print(MidOrPremid().base(linklist))
        # print(MidOrPremid().solution(linklist))
        # if MidOrPremid().base(linklist)!=MidOrPremid().solution(linklist):
        #     print('no')
        #     while linklist:
        #         print(linklist.value)
        #         linklist = linklist.next

        # print(MidOrPostMid().base(linklist))
        # print(MidOrPostMid().solution(linklist))
        # if MidOrPostMid().base(linklist)!=MidOrPostMid().solution(linklist):
        #     print('no')
        #     while linklist:
        #         print(linklist.value)
        #         linklist = linklist.next

        # print(PreMidOrPrePreMid().base(linklist))
        # print(PreMidOrPrePreMid().solution(linklist))
        if PreMidOrPrePreMid().base(linklist)!=PreMidOrPrePreMid().solution(linklist):
            print('no')
            while linklist:
                print(linklist.value)
                linklist = linklist.next
            print('----------')
    print('ok')
