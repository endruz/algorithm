from typing import List
from functools import lru_cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        step = 1
        if stones[1] - stones[0] != step:
            return False

        @lru_cache(None)
        def func(distance, step):
            if distance == stones[-1]:
                return True
            for s in range(step - 1, step + 2):
                if (s > 0) and (distance + s in stones):
                    if func(distance + s, s):
                        return True
            return False

        return func(stones[1], step)
