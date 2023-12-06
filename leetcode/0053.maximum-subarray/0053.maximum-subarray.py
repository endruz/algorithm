from types import List


class Solution1:
    """
    动态规划
    """
    def maxSubArray(self, nums: List[int]) -> int:
        pre, result = 0, nums[0]
        for num in nums:
            pre = max(pre + num, num)
            result = max(result, pre)
        return result


class Solution2:
    """
    分治
    """
    class Status:
        def __init__(self, lSum: int, rSum: int, mSum: int, iSum: int):
            self.lSum = lSum # lSum 表示 [l,r] 内以 ll 为左端点的最大子段和
            self.rSum = rSum # rSum 表示 [l,r] 内以 rr 为右端点的最大子段和
            self.mSum = mSum # mSum 表示 [l,r] 内的最大子段和
            self.iSum = iSum # iSum 表示 [l,r] 的区间和

    def maxSubArray(self, nums: List[int]) -> int:
        return self.getInfo(nums, 0, len(nums) - 1).mSum

    def getInfo(self, arr: List[int], l: int, r: int) -> Status:
        if l == r:
            return self.Status(arr[l], arr[l], arr[l], arr[l])
        m = (l + r) // 2
        lStatus = self.getInfo(arr, l, m)
        rStatus = self.getInfo(arr, m + 1, r)
        return self.pushUp(lStatus, rStatus)

    def pushUp(self, lStatus: Status, rStatus: Status) -> Status:
        iSum = lStatus.iSum + rStatus.iSum
        lSum = max(lStatus.lSum, lStatus.iSum + rStatus.lSum)
        rSum = max(rStatus.rSum, rStatus.iSum + lStatus.rSum)
        mSum = max(lStatus.mSum, rStatus.mSum, lStatus.rSum + rStatus.lSum)
        return self.Status(lSum, rSum, mSum, iSum)
