# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = None
        tmp = 0
        while l1 or l2:
            valSum = 0
            if l1:
                valSum += l1.val
                l1 = l1.next
            if l2:
                valSum += l2.val
                l2 = l2.next
            valSum += tmp
            tmp = valSum // 10
            if head:
                tail.next = ListNode(valSum % 10)
                tail = tail.next
            else:
                head = tail = ListNode(valSum % 10)

        if tmp:
            tail.next = ListNode(tmp)
        return head