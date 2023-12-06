class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i = j = 0
        while i <= len(haystack) - len(needle):
            if haystack[i] == needle[0]:
                j = i
                for char in needle:
                    if char != haystack[j]:
                        break
                    j += 1
                else:
                    return i
            i += 1
        return -1
