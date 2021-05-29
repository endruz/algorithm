class Solution1:
    def intToRoman(self, num: int) -> str:
        def _func(n: int, location: int) -> str:
            if location == 0:
                one, five, ten = "I", "V", "X"
            elif location == 1:
                one, five, ten = "X", "L", "C"
            elif location == 2:
                one, five, ten = "C", "D", "M"
            elif location == 3:
                one, five, ten = "M", "", ""

            if n == 0:
                return ""
            elif 0 < n < 4:
                return one * n
            elif n == 4:
                return f"{one}{five}"
            elif n == 5:
                return five
            elif n < 9:
                return f"{five}{one * (n - 5)}"
            elif n == 9:
                return f"{one}{ten}"

        location, result = 0, list()
        while num:
            result.append(_func(num % 10, location))
            location += 1
            num = num // 10
        return "".join(result[::-1])


class Solution2:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            3: ["", "M", "MM", "MMM"]
        }
        location, result = 0, list()
        while num:
            result.append(hashmap[location][num % 10])
            location += 1
            num = num // 10
        return "".join(result[::-1])


class Solution3:
    def intToRoman(self, num: int) -> str:
        VALUE_SYMBOLS = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        roman = list()
        for value, symbol in VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)
