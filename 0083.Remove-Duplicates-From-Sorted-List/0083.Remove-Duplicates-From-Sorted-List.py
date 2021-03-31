class ListNode:
    '''
    Definition for singly-linked list.
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        新建 pointNode 节点指向 head，防止 head 为 None。返回时直接返回 pointNode.next 即可。
        从 pointNode 开始对链表进行遍历。
        如果当前 currNode 与 currNode.next 值相同，则将 currNode 指向 currNode.next.next。
        '''
        pointNode = ListNode(None, head)
        currNode = pointNode
        while currNode.next:
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        return pointNode.next
