from typing import List


class Solution:
    '''
    双指针
    从后往前比较
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        for index in range(m + n - 1, -1, -1):
            if j < 0:
                break
            elif i < 0 or nums2[j] > nums1[i]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
