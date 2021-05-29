from typing import List


class Solution:
    """
    船舶承载能力一定大于等于所有包裹中最重的那个的重量，一定小于等于所有包裹重量之和
    对这个范围进行二分查找
    """
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_carry, max_carry = max(weights), sum(weights)
        while min_carry < max_carry:
            mid_carry = (min_carry + max_carry) // 2

            curr_carry, day = 0, 1
            for weight in weights:
                if curr_carry + weight > mid_carry:
                    day += 1
                    curr_carry = 0
                curr_carry += weight

            if day <= D:
                max_carry = mid_carry
            elif day > D:
                min_carry = mid_carry + 1
            # 当 day == D 时不能直接 return，因为可能存在 mid_carry - 1 也满足 D 天
            # else:
            #     return mid_carry
        return min_carry
