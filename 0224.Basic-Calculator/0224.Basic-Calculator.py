class Solution:
    def calculate(self, s: str) -> int:
        stack = list()
        index = 0
        length = len(s)

        def cal(s):
            length = len(s)
            num1 = 0
            num2 = ""
            operator = "+"
            for i in range(length):
                if s[i].isdigit():
                    num2 += s[i]
                    if i == length - 1 or s[i+1] in ["+", "-", " "]:
                        if operator == "+":
                            num1 = num1 + int(num2)
                        elif operator == "-":
                            num1 = num1 - int(num2)
                        num2 = ""
                elif s[i] in ["+", "-"]:
                    if i > 0 and s[i-1] == "-":
                        operator = "+" if s[i] == "-" else "-"
                    else:
                        operator = s[i]
            return num1

        while index < length:
            if s[index] == '(':
                stack.append(index)
                index += 1
            elif s[index] == ')':
                start = stack.pop()
                value = str(cal(s[start+1: index]))
                if index == length - 1:
                    s = s[:start] + value
                else:
                    s = s[:start] + value + s[index+1:]
                length = len(s)
                index = start + len(value) - 1
            else:
                index += 1

        return int(cal(s))
