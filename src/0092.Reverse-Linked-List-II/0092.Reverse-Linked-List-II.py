class ListNode:
    '''
    Definition for singly-linked list.
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween1(self, head: ListNode, left: int, right: int) -> ListNode:
        currNode = head
        nodeList = list()
        for i in range(1, right+1):
            if left <= i <= right:
                nodeList.append(currNode)
            currNode = currNode.next
        for i in range(len(nodeList)//2):
            j = -i - 1
            nodeList[i].val, nodeList[j].val = nodeList[j].val, nodeList[i].val
        return head

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        # 在链表前加一个节点，以避免特殊处理 left 为 1 的情况
        # 返回时直接 return pointNode.next
        pointNode = ListNode(-1, head)
        # preNode 是 left 前一个节点
        preNode = pointNode
        for _ in range(1, left):
            preNode = preNode.next
        # currNode 是反转前 left 位置的节点
        currNode = preNode.next

        # 不断把下一个节点移到反转区域的第一个位置
        for _ in range(right - left):
            nextNode = currNode.next
            currNode.next = nextNode.next
            nextNode.next = preNode.next
            preNode.next = nextNode

        return pointNode.next
