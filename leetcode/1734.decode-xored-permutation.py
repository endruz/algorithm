from typing import List

"""
异或运算有如下性质：

- 相同数值异或，结果为 0
- 任意数值与 0 进行异或，结果为数值本身
- 异或本身满足交换律

perm 长度为 n，n 为奇数
perm 是前 n 个正整数的排列，所以 perm 所有元素的异或结果为 1 XOR 2 XOR 3 XOR …… XOR n
perm 所有元素的异或结果记为 a

encode 满足 encoded[i] = perm[i] XOR perm[i + 1]
encode 长度为 n - 1,为偶数

encoded 每隔一个元素进行异或
encoded[1] XOR encoded[3] XOR …… XOR encoded[n - 2]
= perm[1] XOR perm[2] XOR perm[3] XOR perm[4] ……  XOR perm[n - 2] XOR perm[n - 1]
结果为 perm 除了 perm[0] 的所有元素的异或记为 b

a = perm[0] XOR b
两边同时异或 b 得出
a XOR b = perm[0]

得出 perm[0] 的数值后，可推出 perm 其他所有值
"""


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        a = b = 0
        for i in range(1, n + 1):
            a ^= i
        for i in range(1, n, 2):
            b ^= encoded[i]
        perm = [a ^ b]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])
        return perm
