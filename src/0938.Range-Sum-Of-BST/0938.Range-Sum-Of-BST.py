# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def func(node):
            if node is None:
                return
            if low < node.val:
                func(node.left)
            if low <= node.val <= high:
                self.result += node.val
            if node.val < high:
                func(node.right)
        self.result = 0
        func(root)
        return self.result
