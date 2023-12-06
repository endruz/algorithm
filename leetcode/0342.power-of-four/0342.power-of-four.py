from math import sqrt


class Solution1:
    """
    若 n 为 4 的幂，则开平方后为 2 的幂。
    这是问题就转化为 sqrt(n) 是否为 2 的幂的问题。
    """
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (2 ** 30) % sqrt(n) == 0


class Solution2:
    """
    4 的幂和 2 的幂的区别在于二进制中 1 永远在奇数位上。
    所以 4 的幂与二进制中偶数位为 1 的数按位与永远为 0
    题目中 n 最大为 32 位二进制
    (10101010101010101010101010101010)2 转换为 16 进制为 (aaaaaaaa)16
    """
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n & 0xaaaaaaaa == 0
