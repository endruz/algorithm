class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        startChr, columnName = ord("A") - 1, list()
        while columnNumber > 0:
            mod = columnNumber % 26
            columnNumber = columnNumber // 26
            if mod == 0:
                columnNumber -= 1
                mod = 26
            columnName.append(chr(startChr + mod))
        return "".join(columnName[::-1])
