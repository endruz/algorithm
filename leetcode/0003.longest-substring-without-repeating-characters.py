class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        maxLen, end = 0, -1
        for index, value in enumerate(s):
            if value in dic:
                end = max(end, dic[value])
            maxLen = max(maxLen, index - end)
            dic[value] = index
        return maxLen
