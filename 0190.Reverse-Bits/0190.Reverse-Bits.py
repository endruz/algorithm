class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        循环
        每次循环中
        result = result << 1 左移一位以供写入
        n & 1 与运算获取 n 当前最后一位
        result | (n & 1) 获取的最后一位写入
        n = n >> 1 右移一位以便下次循环
        '''
        result = 0
        for _ in range(32):
            result = result << 1
            result = result | (n & 1)
            n = n >> 1
        return result