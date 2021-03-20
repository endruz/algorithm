class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    num = num2 + num1
                elif token == "-":
                    num = num2 - num1
                elif token == "*":
                    num = num2 * num1
                elif token == "/":
                    num = int(num2 / num1)
            stack.append(num)
        return stack[0]