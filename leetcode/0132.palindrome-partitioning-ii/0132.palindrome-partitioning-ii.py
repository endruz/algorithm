class Solution:
    def minCut(self, s: str) -> int:
        '''
        运行超时
        '''
        import sys
        self.minCutCount = sys.maxsize
        length = len(s)

        def isPalindrome(string, left, right):
            '''
            判断子串是否为回文字符串
            左右坐标逐渐向中心靠拢，并判断左右坐标字符是否相同
            若不相同，则不是回文字符串
            若 left >= right 时，则说明该子串已完成遍历，是回文字符串
            '''
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def dfs(string, index, CutCount):
            if CutCount > self.minCutCount:
                return
            elif index < length:
                for i in range(index, length):
                    if isPalindrome(string, index, i):
                        dfs(string, i+1, CutCount+1)
            else:
                self.minCutCount = self.minCutCount if self.minCutCount < CutCount else CutCount

        dfs(s, 0, -1)
        return self.minCutCount
