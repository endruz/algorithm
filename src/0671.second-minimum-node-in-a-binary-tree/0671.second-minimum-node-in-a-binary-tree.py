# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        vals = list()
        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        vals = sorted(list(set(vals)))
        if len(vals) < 2:
            return -1
        else:
            return vals[1]


class Solution2:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result, min_val = 2 ** 31, root.val
        def dfs(node: TreeNode) -> None:
            nonlocal result
            if node is None:
                return
            elif node.val != min_val:
                result = min(node.val, result)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result if result != 2 ** 31 else -1
