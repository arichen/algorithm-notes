# https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.

class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # stack is to hold the unfinished result on each level for later use
        res, sign, num = 0, 1, 0

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + (ord(c) - ord("0"))
            elif c in ("+", "-"):
                res += sign * num
                sign = 1 if c == "+" else -1
                num = 0
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                sign, num = 1, 0

        return res + sign * num