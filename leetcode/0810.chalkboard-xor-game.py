from typing import List
from functools import reduce


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return True if reduce(lambda x, y: x ^ y, nums) == 0 else (len(nums) % 2) == 0
