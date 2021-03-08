class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = list()
        subList = list()
        length = len(s)

        def isPalindrome(string, left, right):
            '''
            判断子串是否为回文字符串
            左右坐标逐渐向中心靠拢，并判断左右坐标字符是否相同
            若不相同，则不是回文字符串
            若 left >= right 时，则说明该子串已完成遍历，是回文字符串
            '''
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def dfs(string, index, subList, result):
            if index < length:
                for i in range(index, length):
                    if isPalindrome(string, index, i):
                        subList.append(string[index: i+1])
                        dfs(string, i+1, subList, result)
                        subList.pop()
            else:
                result.append(subList.copy())

        dfs(s, 0, subList, result)
        return result
