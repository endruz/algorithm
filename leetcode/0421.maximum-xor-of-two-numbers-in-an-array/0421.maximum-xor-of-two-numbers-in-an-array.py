from typing import List


class Solution1:
    """
    暴力破解，超时
    """
    def findMaximumXOR(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        for i in range(n):
            for j in range(i, n):
                if (tmp := nums[i] ^ nums[j]) > result:
                    result = tmp
        return result


class Solution2:
    """
    参考官方解法，哈希表
    """
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 因为 0 <= nums[i] <= 2^31 - 1，所以 nums[i] 转换为二进制后最高位为 30
        HIGHEST_BIT = 30
        # result 为最终结果，计算过程中会不断添加二进制位数
        result = 0

        for i in range(HIGHEST_BIT, -1, -1):
            nums_i_bit = set()
            # 将 nums 中所有元素的第 i 位到最高位的部分存到集合中
            for num in nums:
                nums_i_bit.add(num >> i)

            # result 加一位 1，相当于所有位数进一位后最低位为 1
            # 等价于 result * 2 + 1
            result_add_one_bit = result * 2 + 1
            flag = False

            for num in nums:
                # 由异或的的性质得到
                # nums[i] ^ nums[j] = result => result ^ nums[i] = nums[j]
                if result_add_one_bit ^ (num >> i) in nums_i_bit:
                    flag = True
                    break

            # 当 result_add_one_bit 不满足时，说明最低位为 0。在 result_add_one_bit 上减一即可
            result = result_add_one_bit if flag else result_add_one_bit - 1
        return result
