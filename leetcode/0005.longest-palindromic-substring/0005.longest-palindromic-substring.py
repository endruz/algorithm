class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while 0 <= left <= right and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1, right - left - 1
        left, right, lens = 0, 0, 1
        for i in range(len(s)):
            left1, right1, lens1 = expandAroundCenter(i, i)
            left2, right2, lens2 = expandAroundCenter(i, i + 1)
            if lens1 > lens:
                left, right, lens = left1, right1, lens1
            if lens2 > lens:
                left, right, lens = left2, right2, lens2
        return s[left: right + 1]
