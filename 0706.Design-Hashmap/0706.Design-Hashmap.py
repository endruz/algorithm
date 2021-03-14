class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = list()


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for index in range(len(self.hashMap)):
            if self.hashMap[index][0] == key:
                self.hashMap[index][1] = value
                break
        else:
            self.hashMap.append([key, value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for index in range(len(self.hashMap)):
            if self.hashMap[index][0] == key:
                return self.hashMap[index][1]
        else:
            return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for index in range(len(self.hashMap)):
            if self.hashMap[index][0] == key:
                del self.hashMap[index]
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)