import operator
def evaluate(s: str):
    nums, ops = [], []

    for c in s:
        if c in ("+", "-", "*", "/"):
            ops.append(c)
        elif ops and ops[-1] in ("*", "/"):
            print(c, nums, ops)
            func = operator.mul if ops.pop() == "*" else operator.truediv
            nums.append(func(nums.pop(), int(c)))
        else:
            nums.append(int(c))
    print(nums, ops)

    while ops:
        func = operator.add if ops.pop() == "+" else operator.sub
        b, a = nums.pop(), nums.pop()
        nums.append(func(a, b))

    print(nums)

evaluate("2*3-9/3+1")