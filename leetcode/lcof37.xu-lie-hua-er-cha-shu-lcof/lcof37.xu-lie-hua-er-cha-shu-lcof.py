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
        # print(data)
        return ",".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = deque(data.split(","))

        if vals[0] == "None":
            return None

        root = TreeNode(0)

        def dfs(node: TreeNode) -> None:
            node.val = int(vals.popleft())
            if vals[0] == "None":
                vals.popleft()
            else:
                node.left = TreeNode(0)
                dfs(node.left)

            if vals[0] == "None":
                vals.popleft()
            else:
                node.right = TreeNode(0)
                dfs(node.right)

        dfs(root)
        return root


# Your Codec object will be instantiated and called as such:
root = node = TreeNode(0)
for i in range(1, 5):
    node.left = TreeNode(i)
    node = node.left

codec = Codec()
a = codec.deserialize(codec.serialize(root))

codec.serialize(a)
