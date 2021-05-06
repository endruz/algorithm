from typing import List

"""
异或性质： a ^ b = c  => c ^ a = b
"""


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for n in encoded:
            decoded.append(n ^ decoded[-1])
        return decoded
