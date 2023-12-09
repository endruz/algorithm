from collections import Counter


class Solution1:
    """
    2 的幂即二进制中只有一个 1
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Counter(bin(n)).get('1', 0) == 1


class Solution2:
    """
    原理同 1
    """
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        flag = False
        for i in range(31):
            if (n >> i) & 1 == 1:
                if flag:
                    return False
                else:
                    flag = True
        return flag


class Solution3:
    """
    最大值的约数
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (2 ** 30) % n == 0


class Solution4:
    """
    n 为 2 的幂，例 0100
    n - 1 则为 0011
    n 和 n - 1 按位与则得到 0
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
