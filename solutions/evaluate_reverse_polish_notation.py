class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    value = stack.pop()
                    stack[-1] += value
                case "-":
                    value = stack.pop()
                    stack[-1] -= value
                case "*":
                    value = stack.pop()
                    stack[-1] *= value
                case "/":
                    value = stack.pop()
                    stack[-1] = int(float(stack[-1]) / float(value))
                case _:
                    stack.append(int(token))
        return stack[0]


from leetcode import *

test(Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)
test(Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)
test(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ),
    22,
)
