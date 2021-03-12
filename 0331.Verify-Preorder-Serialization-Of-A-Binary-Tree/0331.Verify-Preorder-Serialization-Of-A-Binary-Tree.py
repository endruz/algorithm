class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = list()
        length = len(preorder)
        if preorder[0] == "#":
            return length == 1
        else:
            stack.append(1)
        for index in range(1, length):
            if preorder[index] == ",":
                continue
            elif preorder[index] == "#":
                try:
                    while stack and stack[-1] == 0:
                        stack.pop()
                        stack.pop()
                except Exception as e:
                    print(f"error: {e}")
                    return False
                stack.append(0)
            else:
                if not preorder[index-1].isdigit():
                    stack.append(1)
        return len(stack) == 1 and not stack[-1]
