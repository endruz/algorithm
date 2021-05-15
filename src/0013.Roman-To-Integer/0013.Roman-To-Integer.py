class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        index, length, value = 0, len(s), 0
        while index < length:
            if index + 1 < length and hashmap[s[index]] < hashmap[s[index + 1]]:
                value += hashmap[s[index + 1]] - hashmap[s[index]]
                index += 2
            else:
                value += hashmap[s[index]]
                index += 1
        return value
