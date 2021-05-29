from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    广度优先遍历（BFS）
    """
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        values = (x, y)
        if root.val in values:
            return False
        nodes = deque([root])

        while nodes:
            flag = False
            for _ in range(len(nodes)):
                node = nodes.popleft()
                f = False
                if node.left:
                    if node.left.val in values:
                        f = True
                        if flag:
                            return True
                        else:
                            flag = True
                    nodes.append(node.left)
                if node.right:
                    if node.right.val in values:
                        if f:
                            return False
                        if flag:
                            return True
                        else:
                            flag = True
                    nodes.append(node.right)
        return False


class Solution2:
    """
    深度优先遍历（DFS）
    """
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parents, x_depth, x_exist = None, None, False
        y_parents, y_depth, y_exist = None, None, False

        def dfs(node: TreeNode, depth: int, parents: TreeNode):
            if node is None:
                return

            nonlocal x_parents, x_depth, x_exist
            nonlocal y_parents, y_depth, y_exist

            if node.val == x:
                x_parents, x_depth, x_exist = parents, depth, True
            elif node.val == y:
                y_parents, y_depth, y_exist = parents, depth, True

            if x_exist and y_exist:
                return

            dfs(node.left, depth + 1, node)

            if x_exist and y_exist:
                return

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_parents != y_parents and x_depth == y_depth
