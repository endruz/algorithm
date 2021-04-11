class Solution:
    def calculate(self, s: str) -> int:
        num = ""
        expression = list()
        length = len(s)

        for i in range(length):
            if s[i].isdigit():
                num += s[i]
                if i + 1 == length or s[i+1] in ["+", "-", "*", "/", " "]:
                    if expression and expression[-1] == "*":
                        expression.pop()
                        value = expression.pop() * int(num)
                        expression.append(value)
                    elif expression and expression[-1] == "/":
                        expression.pop()
                        value = expression.pop() // int(num)
                        expression.append(value)
                    else:
                        expression.append(int(num))
            elif s[i] in ["+", "-", "*", "/"]:
                expression.append(s[i])
                num = ""

        result = 0
        operator = "+"

        for item in expression:
            if isinstance(item, int):
                if operator == "+":
                    result += item
                elif operator == "-":
                    result -= item
            else:
                operator = item

        return result
