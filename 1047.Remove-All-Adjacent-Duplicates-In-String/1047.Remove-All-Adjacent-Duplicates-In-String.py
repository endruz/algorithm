class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = list()
        for i in range(len(S)):
            if stack and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return "".join(stack)

