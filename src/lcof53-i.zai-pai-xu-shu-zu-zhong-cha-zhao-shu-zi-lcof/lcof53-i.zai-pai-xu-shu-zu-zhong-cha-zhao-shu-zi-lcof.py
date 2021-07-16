from types import List


class Solution1:
    """
    一次二分查找
    先使用二分法进行查找，如果没找到返回 0
    如果找到，在分别往他的左边和右边找(因为相同的值在排序数组中是挨着的)
    """
    def search(self, nums: List[int], target: int) -> int:
        n, count = len(nums), 0
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                count += 1
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if not count:
            return 0
        rmid = mid + 1
        lmid = mid - 1
        while lmid >= 0:
            if nums[lmid] == target:
                count += 1
                lmid -= 1
            else:
                break
        while rmid < n:
            if nums[rmid] == target:
                count += 1
                rmid += 1
            else:
                break
        return count


class Solution2:
    """
    一次二分查找
    先使用二分法进行查找到第一个值为 target 的元素的下标，如果没找到返回 0
    如果找到，再往他的右边扫描(因为相同的值在排序数组中是挨着的)
    """
    def search(self, nums: List[int], target: int) -> int:
        n, count = len(nums), 0
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        while 0 <= right < n and nums[right] == target:
            count += 1
            right += 1
        return count


class Solution3:
    """
    两次二分查找
    分别找到
    第一个值为 target 的元素的下标 indexl
    最后一个值为 target 的元素的下标 indexr
    返回值为 indexr - indexl + 1
    """
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        # 获取 indexl
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return 0
        indexl = left
        # 获取 indexr
        left, right = 0, n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[left] != target:
            return 0
        indexr = left
        return indexr - indexl + 1
