from types import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = sorted(Counter(nums).items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        if counter[0][1] > len(nums) // 2:
            return counter[0][0]
        return -1


class Solution2:
    """
    超过半数和不超过半数的值最大的区别是什么?

    当我们扫描一遍下来的时候，直接进行一个只要两个不同就可以消除的消消乐，如果有超过半数的值，那么剩下的这个值必然是它。
    这是因为其他值总共也没有这个值的人数多，所以不管怎么消除，这个值都会留下来。
    (注意: 只有超过半数才一定会最终留下来，连等于半数都不一定是最终留下来的结果。而即使小于等于半数的留下来，也无法通过第二轮验证)

    全部消除后count为0，即可以两两消除，必然不存在超过半数的值，不用进行第二轮验证。

    第二轮验证:

    原数组没有超过半数的值的时候，也可能有剩下的值。
    比如说 [1,2,3],在消除过后仍然可以得到3。
    所以还需要遍历一遍统计上轮发现的值的个数，确保它是超过半数的。
    """
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 0, -1
        for num in nums:
            if count == 0:
                result = num
                count += 1
            elif num == result:
                count += 1
            else:
                count -= 1
        return result if count and nums.count(result) > len(nums) // 2 else -1
