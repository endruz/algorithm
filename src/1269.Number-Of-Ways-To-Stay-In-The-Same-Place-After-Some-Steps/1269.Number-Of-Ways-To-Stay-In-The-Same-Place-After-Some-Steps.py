class Solution:
    """
    dp[i][j] 为第 i 步到达 j 处的方案数
    dp[i][j] = dp[i−1][j] + dp[i−1][j−1] + dp[i−1][j+1]
    """
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        # 可移动的最远距离，当移动距离 >= steps//2+1 时,一定无法返回 0 处
        maxLen = min(steps // 2 + 1, arrLen)
        # 不能使用这个来初始化数组! 会导致数组中的子一维数组地址都是一样, 改动一个其他都会改变
        # dp = [[0] * arrLen] * (steps + 1)
        dp = [[0 for _ in range(maxLen)] for _ in range(steps + 1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for i in range(1, steps + 1):
            for j in range(maxLen):
                # 因为要返回 dp[steps][0] 的值,则对角线外的数值无用
                if i + j > steps:
                    break
                dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if j + 1 < maxLen:
                    dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= MOD
        return dp[steps][0]
