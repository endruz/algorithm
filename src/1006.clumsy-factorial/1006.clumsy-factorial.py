class Solution1:
    def clumsy(self, N: int) -> int:
        '''
        遇到 "*" 和 "/" 先出栈计算，之后将结果入栈。
        遇到 "-"，取反后入栈。取反后，负数的除法结果就不再是地板除法需要向上取整。正数的除法依旧是向下取整（地板除法）。结合起来就是向零取整。
        遇到 "+"，直接入栈。

        向零取整方法：
        1. 根据情况使用 math 库里的 floor 函数（向下取整，相当于运算符 "//"） 和 ceil 函数（向上取整）
        2. int(num1 / float(num2))
        3. 使用库函数 operator.truediv(num1, num2)
        '''
        from math import floor
        from math import ceil
        expression = [N]
        operators = ["*", "/", "+", "-"]
        index = 0
        for value in range(N-1, 0, -1):
            if operators[index] == "*":
                expression.append(expression.pop() * value)
            elif operators[index] == "/":
                if (tmp := (expression.pop() / value)) >= 0:
                    expression.append(floor(tmp))
                else:
                    expression.append(ceil(tmp))
            elif operators[index] == "+":
                expression.append(value)
            else:
                expression.append(-value)
            index = 0 if index == 3 else index + 1
        return sum(expression)


class Solution2:
    def clumsy(self, N: int) -> int:
        '''
        Solution1 的优化
        优化点：
        1. 不使用操作符集合，直接整型替代。*/+- 分别对应 0123
        2. 向零取整使用 int(num1 / float(num2))
        '''
        expression = [N]
        operator = 0
        for value in range(N-1, 0, -1):
            if operator == 0:
                expression.append(expression.pop() * value)
            elif operator == 1:
                expression.append(int(expression.pop() / float(value)))
            elif operator == 2:
                expression.append(value)
            else:
                expression.append(-value)
            operator = (operator + 1) % 4
        return sum(expression)
