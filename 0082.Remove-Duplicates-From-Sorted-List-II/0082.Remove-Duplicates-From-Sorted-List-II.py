# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        新建 pointNode 节点指向 head，防止 head 重复丢失链表。返回时直接返回 pointNode.next 即可。
        从 pointNode 开始对链表进行遍历。
        如果当前 currNode.next 与 currNode.next.next 值相同，则记录值 value，并将后面具有相同值的节点全部删除。
        '''
        pointNode = ListNode(None, head)
        currNode = pointNode

        while currNode.next and currNode.next.next:
            if currNode.next.val == currNode.next.next.val:
                value = currNode.next.val
                while currNode.next and currNode.next.val == value:
                    currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        return pointNode.next

