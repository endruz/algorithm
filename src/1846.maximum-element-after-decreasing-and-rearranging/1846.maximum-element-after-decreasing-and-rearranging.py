from types import List


class Solution1:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr, result = sorted(arr), 1
        for num in arr:
            if num >= result:
                result += 1
        return result - 1


class Solution2:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        return arr[-1]
