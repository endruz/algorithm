# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator1:
    '''
    提前保存全部节点
    因为是中序遍历（首先遍历左子树，然后访问根结点，最后遍历右子树）。
    所以在 __init__() 中以首先遍历右子树，然后访问根结点，最后遍历左子树的方式提前将所有数据存入栈中。
    hasNext()直接判断当前栈的长度
    next()直接 pop 栈顶数据并返回
    '''

    def __init__(self, root: TreeNode):
        def _BST2Stack(root, stack):
            if not root: return
            _BST2Stack(root.right, stack)
            stack.append(root.val)
            _BST2Stack(root.left, stack)
        self.stack = list()
        _BST2Stack(root, self.stack)

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop()
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        return bool(len(self.stack))

class BSTIterator2:
    '''
    迭代时计算 next  节点
    __init__() 从根节点开始，将所有左节点存入栈中
    hasNext()直接判断当前栈的长度
    next()
    1. 直接 pop 栈顶节点
    2. 判断栈顶节点是否存在右节点，若存在则从栈顶节点的右节点开始，将所有左节点存入栈中
    3. 最后返回栈顶节点的值
    '''
    def __init__(self, root: TreeNode):
        self.stack = list()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if self.hasNext():
            nextValue = self.stack.pop()
            node = nextValue.right
            while node:
                self.stack.append(node)
                node = node.left
            return nextValue.val
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        return bool(len(self.stack))

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()