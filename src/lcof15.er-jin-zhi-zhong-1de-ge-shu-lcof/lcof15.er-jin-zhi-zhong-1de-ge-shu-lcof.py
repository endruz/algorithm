class Solution1:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & 2 ** i:
                count += 1
        return count
