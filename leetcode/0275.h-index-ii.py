from types import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            h = n - mid
            if h <= citations[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
