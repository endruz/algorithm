# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    '''
    二叉搜索树（BST）的中序遍历是有序的
    中序遍历所有值并保存进数组中
    计算所有相邻的两个值之间的差，返回最小的那一个
    '''
    def minDiffInBST(self, root: TreeNode) -> int:
        values = list()

        def insert_value(node):
            if not node:
                return
            insert_value(node.left)
            values.append(node.val)
            insert_value(node.right)

        insert_value(root)
        result = 10**5
        for i in range(0, len(values) - 1):
            result = min(values[i + 1] - values[i], result)
        return result


class Solution2:
    '''
    二叉搜索树（BST）的中序遍历是有序的
    中序遍历的过程中计算当前节点和上一个节点的差
    返回最小的那一个
    '''
    def minDiffInBST(self, root: TreeNode) -> int:
        prevalue = None
        result = 10**5

        def compare(node):
            nonlocal prevalue
            nonlocal result
            if not node:
                return
            compare(node.left)
            if prevalue:
                result = min(node.val - prevalue, result)
            prevalue = node.val
            compare(node.right)

        compare(root)
        return result
