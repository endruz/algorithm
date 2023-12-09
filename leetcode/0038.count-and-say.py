class Solution:
    def countAndSay(self, n: int) -> str:
        nums = "1"
        for i in range(1, n):
            num, count = nums[0], 0
            result = ''
            for i in range(len(nums)):
                if num == nums[i]:
                    count += 1
                else:
                    result += f'{count}{num}'
                    num, count = nums[i], 1
            else:
                result += f'{count}{num}'
            nums = result
        return nums
