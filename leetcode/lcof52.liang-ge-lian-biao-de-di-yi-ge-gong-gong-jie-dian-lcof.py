# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """
    哈希集合
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node = headA
        address_set = set()
        while node is not None:
            address_set.add(id(node))
            node = node.next

        node = headB
        while node is not None:
            address = id(node)
            if address in address_set:
                return node
            node = node.next
        return None


class Solution2:
    """
    双指针
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
