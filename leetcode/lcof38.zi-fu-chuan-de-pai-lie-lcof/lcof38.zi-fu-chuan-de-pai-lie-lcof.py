from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        s_list, result, n = list(s), list(), len(s)

        def dfs(index: int) -> None:
            if index == n - 1:
                result.append("".join(s_list))
                return

            char_set = list()
            for i in range(index, n):
                if s_list[i] in char_set:
                    continue
                char_set.append(s_list[i])
                s_list[index], s_list[i] = s_list[i], s_list[index]
                dfs(index + 1)
                s_list[index], s_list[i] = s_list[i], s_list[index]

        dfs(0)
        return result
