class ListNode:
    '''
    Definition for singly-linked list.
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        先计算出链表的长度 length
        再将链表连成一个环
        当有右移次数 k 为 length 的倍数时，相当于没有移动过
        所以实际右移次数为 k % length
        这时头节点为 head 后退 k % length 次的的节点
        又因为链表无法后退，所以等价于 head 前进 length - k % length 次的节点
        找到头节点后断开环，即是返回结果

        根据题意可发现以下几种特殊情况，返回原本链表即可
        1. length <= 1
        2. k = 0
        3, length - k % length = length
        '''
        if not head or not head.next or k == 0:
            return head
        length = 1
        pointNode = head
        while pointNode.next:
            length += 1
            pointNode = pointNode.next

        # 海象表达式（:=）把表达式的一部分赋值给变量，Python3.8 新特性
        if (step := length - k % length) == length:
            return head

        pointNode.next = head
        for i in range(step):
            pointNode = head
            head = head.next
        else:
            pointNode.next = None
        return head
