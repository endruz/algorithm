from typing import List

"""
当 m * k > n 时说明花园中的花朵数量不满足制作 m 束花，直接返回 -1
反之，最少等待天数在 [min(bloomDay), max(bloomDay)] 中，可使用二分法来确定最少天数。
"""


class Solution1:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def check(bloomDay: List[int], day: int):
            check_list = [0 if day < d else 1 for d in bloomDay]
            count = index = 0
            while index <= n - k:
                if check_list[index]:
                    for _ in range(1, k):
                        index += 1
                        if not check_list[index]:
                            break
                    else:
                        count += 1
                index += 1
            if count < m:
                return False
            else:
                return True

        # left, right = min(bloomDay), max(bloomDay)
        left, right = 1, 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if check(bloomDay, mid):
                right = mid
            else:
                left = mid + 1
        return left


class Solution2:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def check(bloomDay: List[int], day: int):
            count = flowers = 0
            for d in bloomDay:
                if d > day:
                    flowers = 0
                else:
                    flowers += 1
                    if flowers == k:
                        count += 1
                        flowers = 0
                    if count == m:
                        return True
            return False

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if check(bloomDay, mid):
                right = mid
            else:
                left = mid + 1
        return left
