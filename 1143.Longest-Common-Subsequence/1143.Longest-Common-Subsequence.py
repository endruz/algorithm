class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1, length2 = len(text1), len(text2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(1, length1+1):
            for j in range(1, length2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[length1][length2]
