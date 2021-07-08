from types import List


class Solution1:
    """
    暴力解法，超时
    """
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count, n, m = 0, len(nums), goal if goal else 1
        for j in range(m, n + 1):
            for i in range(n - j + 1):
                if sum(nums[i:i + j]) == goal:
                    count += 1
        return count


class Solution2:
    """
    哈希表
    """
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count, sum, hashmap = 0, 0, dict()
        for num in nums:
            hashmap[sum] = hashmap.get(sum, 0) + 1
            sum += num
            count += hashmap.get(sum - goal, 0)
        return count
