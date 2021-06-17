from enum import Enum


class Solution1:
    def isDecimal(self, s: str) -> bool:
        if s and s[0] in ["+", "-"]:
            s = s[1:]
        nums = s.split(".")
        if len(nums) == 2:
            if not (flag0 := nums[0].isdigit()) and nums[0]:
                return False
            if not (flag1 := nums[1].isdigit()) and nums[1]:
                return False
            return flag0 or flag1
        else:
            return False

    def isInteger(self, s: str) -> bool:
        if s and s[0] in ["+", "-"]:
            s = s[1:]
        return s.isdigit()

    def isNumber(self, s: str) -> bool:
        def func(char: str):
            nums = s.split(char)
            n, flag = len(nums), False
            if n < 3:
                flag = self.isDecimal(nums[0]) or self.isInteger(nums[0])
                if n == 2:
                    flag = flag and self.isInteger(nums[1])
            return flag

        if func("e"):
            return True
        else:
            return func("E")


class Solution2:
    def isNumber(self, s: str) -> bool:
        state = Enum("state", [
            "init",
            "sign",
            "digit",
            "point",
            "point_start",
            "point_digit",
            "exp",
            "exp_sign",
            "exp_digit",
        ])

        charType = Enum("charType", [
            "sign",
            "digit",
            "point",
            "exp",
            "illegal"
        ])

        transform = {
            state.init: {
                charType.sign: state.sign,
                charType.digit: state.digit,
                charType.point: state.point_start
            },
            state.sign: {
                charType.digit: state.digit,
                charType.point: state.point_start
            },
            state.digit: {
                charType.digit: state.digit,
                charType.point: state.point,
                charType.exp: state.exp
            },
            state.point: {
                charType.digit: state.point_digit,
                charType.exp: state.exp
            },
            state.point_start: {
                charType.digit: state.point_digit,
            },
            state.point_digit: {
                charType.digit: state.point_digit,
                charType.exp: state.exp
            },
            state.exp: {
                charType.sign: state.exp_sign,
                charType.digit: state.exp_digit
            },
            state.exp_sign: {
                charType.digit: state.exp_digit
            },
            state.exp_digit: {
                charType.digit: state.exp_digit
            }
        }

        def toCharType(char: str) -> charType:
            if char.isdigit():
                return charType.digit
            elif char in ["+", "-"]:
                return charType.sign
            elif char == ".":
                return charType.point
            elif char in ["e", "E"]:
                return charType.exp
            else:
                return charType.illegal

        currState = state.init
        for char in s:
            currType = toCharType(char)
            if currType not in transform[currState]:
                return False
            currState = transform[currState][currType]

        return currState in [state.digit,
                             state.point,
                             state.point_digit,
                             state.exp_digit]
