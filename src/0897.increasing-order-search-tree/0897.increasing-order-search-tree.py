# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.pointNode = TreeNode()
        self.currNode = self.pointNode

        def func(node: TreeNode):
            if node is None:
                return
            func(node.left)
            node.left = None
            self.currNode.right = node
            self.currNode = node
            func(node.right)

        func(root)
        return self.pointNode.right
