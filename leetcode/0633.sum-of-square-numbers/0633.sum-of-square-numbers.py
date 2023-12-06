from math import sqrt

"""
因为 a^2 + b^2 = c ，所以 0 < a, b < int(sqrt(c))。
sqrt() 返回一个数的平方根，返回值是 float 类型。
使用 int() 去除小数部分，强制转换成 int 类型。
"""


class Solution1:
    """
    数学法
    b 满足 sqrt(c - a**2)，当 b 为整数时，符合题意返回 True
    """
    def judgeSquareSum(self, c: int) -> bool:
        if c in (0, 1):
            return True
        for a in range(0, int(sqrt(c)) + 1):
            b = sqrt(c - a**2)
            if b - int(b) == 0:
                return True
        return False


class Solution2:
    """
    双指针
    设 a, b = 0, int(sqrt(c))，判断 a^2+b^2 和 c 的大小，进而移动指针位置，从而找寻到最终解
    """
    def judgeSquareSum(self, c: int) -> bool:
        if c in (0, 1):
            return True
        a, b = 0, int(sqrt(c))
        while a <= b:
            sum_ = a ** 2 + b ** 2
            if sum_ > c:
                b -= 1
            elif sum_ < c:
                a += 1
            else:
                return True
        return False
