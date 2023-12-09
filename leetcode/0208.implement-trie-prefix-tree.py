from typing import List


class Trie1:
    class Node:
        def __init__(self, val: str, children: List) -> None:
            self.val = val
            self.children = children

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node(None, [])

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for i in word:
            for child in currNode.children:
                if child and child.val == i:
                    currNode = child
                    break
            else:
                tmp = self.Node(i, [])
                currNode.children.append(tmp)
                currNode = tmp
        if None not in currNode.children:
            currNode.children.append(None)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for i in word:
            for child in currNode.children:
                if child and child.val == i:
                    currNode = child
                    break
            else:
                return False
        if None not in currNode.children:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for i in prefix:
            for child in currNode.children:
                if child and child.val == i:
                    currNode = child
                    break
            else:
                return False
        return True


class Trie2:
    class Node:
        def __init__(self) -> None:
            self.isEnd = False
            self.children = [None] * 26

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for i in word:
            index = ord(i) - ord('a')
            if not currNode.children[index]:
                currNode.children[index] = self.Node()
            currNode = currNode.children[index]
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for i in word:
            index = ord(i) - ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]
        if not currNode.isEnd:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for i in prefix:
            index = ord(i) - ord('a')
            if not currNode.children[index]:
                return False
            currNode = currNode.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
