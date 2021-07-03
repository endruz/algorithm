from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        charCounter = sorted(Counter(s).items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        charCounter = [char[0]*char[1] for char in charCounter]
        return "".join(charCounter)
