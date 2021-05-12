from typing import List


class Solution1:
    """
    暴力破解，超时
    """
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = list()
        for i in queries:
            val = 0
            for j in range(i[0], i[1] + 1):
                val ^= arr[j]
            result.append(val)
        return result


class Solution2:
    """
    异或运算有如下性质：

    - 相同数值异或，结果为 0
    - 任意数值与 0 进行异或，结果为数值本身
    - 异或本身满足交换律

    生成列表 xor 满足

    - 当 i = 0 时， xor[i] = 0
    - 当 i > 0 时, xor[i] = arr[0] ^ arr[1] ^ …… ^ arr[i - 1]

    记 queries[i][0] 为 left, queries[i][1] 为 right
    result[i] = arr[left] ^ arr[left + 1] ^ ... ^ arr[right]
              = (arr[0] ^ arr[left - 1]) ^ (arr[0] ^ arr[right])
              = xor[left] ^ xor[right + 1]
    """
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor, result = [0], list()
        for a in arr:
            xor.append(xor[-1] ^ a)

        for left, right in queries:
            result.append(xor[left] ^ xor[right + 1])
        return result
