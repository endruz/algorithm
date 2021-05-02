from types import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hashmap, count, n = dict(), 0, len(wall)
        for i in range(n):
            width = 0
            for index in range(len(wall[i]) - 1):
                width += wall[i][index]
                hashmap[width] = hashmap.get(width, 0) + 1
                if count < hashmap[width]:
                    count = hashmap[width]
        return n - count
