class Solution:
    '''
    判断一个整数的因数是否仅由 2、3、5 构成。
    只需要把 n 对 2、3、5 整除，看最后是否仅剩下 1。
    0 和负数都不是丑数
    0 的因数没有 2、3、5；
    负数的因数中一定有一个负数。
    '''
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return n == 1
