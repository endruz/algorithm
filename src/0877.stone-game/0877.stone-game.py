from typing import List


class Solution1:
    """
    数学

    假设有 n 堆石子，n 是偶数，则每堆石子的下标从 0 到 n−1。
    根据下标将 n 堆石子分成两组，每组有 n/2 堆石子，下标为偶数的石子堆属于第一组，下标为奇数的石子堆属于第二组。

    初始时，行的开始处的石子堆位于下标 0，属于第一组，行的结束处的石子堆位于下标 n−1，属于第二组。
    因此作为先手的 Alex 可以自由选择取走第一组的一堆石子或者第二组的一堆石子。

    如果 Alex 取走第一组的一堆石子，则剩下的部分在行的开始处和结束处的石子堆都属于第二组，因此 Lee 只能取走第二组的一堆石子。
    如果 Alex 取走第二组的一堆石子，则剩下的部分在行的开始处和结束处的石子堆都属于第一组，因此 Lee 只能取走第一组的一堆石子。

    无论 Lee 取走的是开始处还是结束处的一堆石子，剩下的部分在行的开始处和结束处的石子堆一定是属于不同组的，
    因此轮到 Alex 取走石子时，Alex 又可以在两组石子之间进行自由选择。

    根据上述分析可知，作为先手的 Alex 可以在第一次取走石子时就决定取走哪一组的石子，并全程取走同一组的石子。既然如此，Alex 是否有必胜策略？

    答案是肯定的。将石子分成两组之后，可以计算出每一组的石子数量，同时知道哪一组的石子数量更多。Alex 只要选择取走数量更多的一组石子即可。因此，Alex 总是可以赢得比赛。
    """
    def stoneGame(self, piles: List[int]) -> bool:
        return True


class Solution2:
    """
    动态规划
    """
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n-1] > 0


class Solution3:
    """
    方法二的优化
    """
    def stoneGame(self, piles: List[int]) -> bool:
        n, dp = len(piles), piles.copy()

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[n-1] > 0
