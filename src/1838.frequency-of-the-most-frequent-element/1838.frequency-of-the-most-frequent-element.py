from types import List


class Solution:
    """
    先对原数组 nums 进行从小到大排序，如果存在真实最优解 len，意味着至少存在一个大小为 len 的区间 [l,r]，使得在操作次数不超过 k 的前提下，区间 [l,r] 的任意值 nums[i] 的值调整为 nums[r]。

    这引导我们利用「数组有序」&「前缀和」快速判断「某个区间 [l,r] 是否可以在 kk 次操作内将所有值变为 nums[r]」：

    具体的，我们可以二分答案 len 作为窗口长度，利用前缀和我们可以在 O(1) 复杂度内计算任意区间的和，同时由于每次操作只能对数进行加一，即窗口内的所有数最终变为 nums[r] ，最终目标区间和为 nums[r]∗len，通过比较目标区间和和真实区间和的差值，我们可以知道 k 次操作是否能将当前区间变为 nums[r]。

    上述判断某个值 len 是否可行的 check 操作复杂度为 O(n)，因此算法复杂度为 O(nlogn)。
    """
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        sums = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        def check(len: int) -> bool:
            for i in range(n - len + 1):
                right = i + len - 1
                target = nums[right] * len
                real = sums[right + 1] - sums[i]
                if target - real <= k:
                    return True
            return False

        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left
