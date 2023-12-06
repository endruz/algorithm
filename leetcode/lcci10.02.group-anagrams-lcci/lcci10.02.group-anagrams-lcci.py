from types import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for st in strs:
            key = "".join(sorted(st))
            hashmap.setdefault(key, list()).append(st)
        return list(hashmap.values())
