from types import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = list()
        # 确保同位置处先处理左边缘坐标再处理右边缘坐标
        for building in buildings:
            positions.append((building[0], -building[2]))
            positions.append((building[1], building[2]))
        positions = sorted(positions, key=lambda x: (x[0], x[1]))
        # print(positions)

        handling = [0]
        cur_highest = pre_highest = 0
        result = list()

        for pos, height in positions:
            if height < 0:
                handling.append(-height)
            else:
                handling.remove(height)

            cur_highest = max(handling)
            if pre_highest != cur_highest:
                result.append((pos, cur_highest))
                pre_highest = cur_highest
        return result
