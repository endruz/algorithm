from functools import lru_cache


class Solution:
    '''
    当 s1 和 s2 长度不一致时，则一定不为扰乱字符串；
    当 s1 == s2 时，则一定为扰乱字符串；
    当 s1 和 s2 每个字符的个数不同时，则一定不为扰乱字符串；

    遍历所有可能分割的下标，分以下两种情况：
    1. 交换分割后的两个子字符串
    2. 保持这两个子字符串的顺序不变
    按这两种情况分别递归处理

    在 Python 中，有一个实现记忆化递归的神器，就是 functool 模块的 lru_cache 装饰器。
    它可以把函数的输入和输出结果缓存住，在后续调用中如果遇到了相同的输入，直接从缓存里面读。
    顾名思义，它使用的是 LRU （最近最少使用）的缓存淘汰策略。

    @functools.lru_cache(maxsize=None, typed=False)
    maxsize 为最多缓存次数，如果为 None，则无限制；
    typed=True 时，表示不同参数类型的调用将分别缓存。
    '''
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        from collections import Counter
        length = len(s1)
        if length != len(s2):
            return False
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
