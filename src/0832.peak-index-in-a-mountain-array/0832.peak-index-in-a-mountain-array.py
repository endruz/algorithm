from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid]:
                if arr[mid] < arr[mid + 1]:
                    left = mid + 1
                else:
                    return mid
            else:
                right = mid
