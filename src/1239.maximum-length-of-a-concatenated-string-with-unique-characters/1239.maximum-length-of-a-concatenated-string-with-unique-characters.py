from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                num = ord(ch) - ord("a")
                if (mask >> num) & 1:
                    mask = 0
                    break
                mask |= 1 << num
            if mask:
                masks.append(mask)

        result, n = 0, len(masks)

        def traceback(pos: int, mask: int) -> None:
            if pos == n:
                nonlocal result
                result = max(result, bin(mask).count("1"))
                return

            if mask & masks[pos] == 0:
                traceback(pos + 1, mask | masks[pos])
            traceback(pos + 1, mask)

        traceback(0, 0)
        return result
