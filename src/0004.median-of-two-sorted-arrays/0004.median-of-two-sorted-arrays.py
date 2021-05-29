from typing import List


class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        index = length // 2
        if length % 2 == 1:
            return nums[index]
        else:
            return (nums[index] + nums[index - 1])/2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        nums = list()
        length = len(nums1) + len(nums2)
        index = length // 2
        while True:
            if not nums1:
                nums.extend(nums2[::-1])
            elif not nums2:
                nums.extend(nums1[::-1])
            elif nums1[-1] > nums2[-1]:
                nums.append(nums1.pop())
            else:
                nums.append(nums2.pop())
            if len(nums) > index:
                break
        if length % 2 == 1:
            return nums[index]
        else:
            return (nums[index] + nums[index - 1])/2
