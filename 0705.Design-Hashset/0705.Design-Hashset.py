class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = list()


    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        for index in range(len(self.hashSet)):
            if self.hashSet[index] == key:
                del self.hashSet[index]
                return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for index in range(len(self.hashSet)):
            if self.hashSet[index] == key:
                return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)