class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = - 2 ** 31, 2 ** 31 - 1
        result, flag = 0, x < 0
        while x != 0:
            digit = x % 10
            # x 为负数时，上一步取模运算也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if flag and 0 < digit <= 9:
                digit -= 10
            # x 为负数时，整数除法会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            result = result * 10 + digit
            if not MIN <= result <= MAX:
                return 0
        return result
