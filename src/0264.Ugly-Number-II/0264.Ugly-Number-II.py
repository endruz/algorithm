class Solution:
    '''
    动态规划
    用还没乘过 2 的最小丑数乘以 2；
    用还没乘过 3 的最小丑数乘以 3；
    用还没乘过 5 的最小丑数乘以 5。
    然后在得到的数字中取最小，就是新的丑数。
    注意：下面判断 ugly_list[i] 和 ugly2，ugly3，ugly5 值时，不能用 if-elif-else
    以防止 ugly2，ugly3，ugly5 有相同值时，重复插入的情况
    '''
    def nthUglyNumber(self, n: int) -> int:
        ugly_list = [1] * n
        index2 = index3 = index5 = 0
        for i in range(1, n):
            ugly2 = 2 * ugly_list[index2]
            ugly3 = 3 * ugly_list[index3]
            ugly5 = 5 * ugly_list[index5]
            ugly_list[i] = min(ugly2, ugly3, ugly5)
            if ugly_list[i] == ugly2:
                index2 += 1
            if ugly_list[i] == ugly3:
                index3 += 1
            if ugly_list[i] == ugly5:
                index5 += 1
        return ugly_list[-1]
