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

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def _gen(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    yield nested.getInteger()
                else:
                    yield from _gen(nested.getList())
        self.iterator = _gen(nestedList)
        try:
            self.nextValue = next(self.iterator)
        except StopIteration:
            self.nextValue = None

    def next(self) -> int:
        result = self.nextValue
        try:
            self.nextValue = next(self.iterator)
        except StopIteration:
            self.nextValue = None
        return result

    def hasNext(self) -> bool:
        return self.nextValue is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
