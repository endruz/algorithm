class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in dp:
            i[-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]
