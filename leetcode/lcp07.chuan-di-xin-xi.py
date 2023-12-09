from types import List


class Solution:
    """
    深度优先遍历
    """
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        relation_dict = {i: list() for i in range(n)}
        for r in relation:
            relation_dict[r[0]].append(r[1])

        count, target = 0, n - 1

        def dfs(who: int, round: int) -> None:
            nonlocal count
            flag = False
            if round == k:
                flag = True
            for towho in relation_dict[who]:
                if flag:
                    if towho == target:
                        count += 1
                else:
                    dfs(towho, round + 1)

        dfs(0, 1)
        return count
