from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs1, leafs2 = list(), list()

        def get_leafs(node: TreeNode, leafs: List[str]):
            if not node:
                return
            if node.left is None and node.right is None:
                leafs.append(node.val)
            else:
                get_leafs(node.left, leafs)
                get_leafs(node.right, leafs)

        get_leafs(root1, leafs1)
        get_leafs(root2, leafs2)

        return leafs1 == leafs2
