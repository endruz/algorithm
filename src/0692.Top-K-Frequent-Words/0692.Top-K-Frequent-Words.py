import heapq
from typing import List
from collections import Counter


class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = Counter(words)
        heap = []

        for word, fre in cnt.items():
            heapq.heappush(heap, Word(word, fre))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse=True)
        return [x.word for x in heap]
