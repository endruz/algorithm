from typing import List


class Solution1:
    """
    枚举，超时
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        for i in range(1, n):
            for j in range(n - i + 1):
                if sum(nums[j: j+i]) == k:
                    count += 1
        return count


class Solution2:
    """
    枚举，超时
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, n = 0, len(nums)
        for start in range(n):
            sum = 0
            for end in range(start, n):
                sum += nums[end]
                if sum == k:
                    count += 1
        return count


class Solution3:
    """
    前缀和 + 哈希表优化
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, pre = 0, 0
        hashmap = {0: 1}
        for num in nums:
            pre += num
            if pre - k in hashmap.keys():
                count += hashmap[pre - k]
            hashmap[pre] = hashmap.get(pre, 0) + 1
        return count
