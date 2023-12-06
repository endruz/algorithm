from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []

        def dfs(node: TreeNode) -> None:
            if node is None:
                data.append("None")
                return
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(","))
        if data[0] == "None":
            return None

        def dfs(node: TreeNode) -> None:
            node.val = int(data.popleft())

            if data[0] == "None":
                data.popleft()
            else:
                node.left = TreeNode(0)
                dfs(node.left)

            if data[0] == "None":
                data.popleft()
            else:
                node.right = TreeNode(0)
                dfs(node.right)

        root = TreeNode(0)
        dfs(root)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
