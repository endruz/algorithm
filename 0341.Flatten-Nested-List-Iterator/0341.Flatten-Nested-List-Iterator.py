# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator1:
    '''
    生成器解法
    在初始化时，赋值生成函数，并使用调用一次赋值给属性 nextValue。
    nextValue 存储下一次迭代的值，若为 None 则说明已迭代完毕。
    '''
    def __init__(self, nestedList: [NestedInteger]):
        def _gen(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    yield nested.getInteger()
                else:
                    # for item in _gen(nested.getList()): yield item
                    yield from _gen(nested.getList())
        self.iterator = _gen(nestedList)
        try:
            self.nextValue = next(self.iterator)
        except StopIteration:
            self.nextValue = None

    def next(self) -> int:
        if self.hasNext():
            result = self.nextValue
            try:
                self.nextValue = next(self.iterator)
            except StopIteration:
                self.nextValue = None
            return result
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        return self.nextValue is not None

class NestedIterator2:
    '''
    递归解法
    初始化时遍历输入的嵌套列表所有的元素，判断每个元素是 int 还是 list：
        - 如果当前元素是 int，放入队列尾部；
        - 如果当前元素是 list，那么需要对当前 子list 继续递归。
    '''
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    self.iterator.append(nested.getInteger())
                else:
                    dfs(nested.getList())
        self.iterator = list()
        dfs(nestedList)

    def next(self) -> int:
        if self.hasNext():
            return self.iterator.pop(0)
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        return bool(self.iterator)

class NestedIterator3:
    '''
    栈解法
    与递归解法不同的是，不在初始化时将所有元素全部遍历，在每次调用 hasNext() 方法时操作。
    在初始化时，把嵌套列表的元素逆序放入栈中。
    在 hasNext() 方法中，访问（不弹出）栈顶元素，判断是否为 int：
        - 如果是 int 那么说明有下一个元素，返回 true；然后 next() 就会被调用，把栈顶的 int 弹出；
        - 如果是 list 需要把当前列表的各个元素（不用摊平）逆序放入栈中；
        - 如果栈为空，那么说明原始的嵌套列表已经访问结束了，返回 false。
    必须要在 hasNext() 方法中将 子list 摊平判断，不然在输入为 [[]] 的情况会出错。
    '''
    def __init__(self, nestedList: [NestedInteger]):
        self.iterator = nestedList[::-1]

    def next(self) -> int:
        if self.hasNext():
            return self.iterator.pop().getInteger()
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        while self.iterator:
            if self.iterator[-1].isInteger():
                return True
            else:
                nested = self.iterator.pop().getList()
                while nested:
                    self.iterator.append(nested.pop())
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
