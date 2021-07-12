from types import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        n, i = len(citations), 0
        while i < n and citations[i] > i:
            i += 1
        return i
