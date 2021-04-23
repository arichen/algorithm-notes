from typing import List
"""
giving a list of boxes (w, d, h), return the max height it can be stacked.
a box can only sit on surface strictly larger than itself. (both w, d of top box need to be smaller than bottom box)
cannot rotate the box
"""

""" Solution 1: Recursion """
class Solution1:
    def __init__(self, boxes: List[List[int]]):
        self.boxes = sorted(boxes, key=lambda x: -x[0])
        self.n = len(self.boxes)
        self.res = 0

    def max_stack_height(self):
        self._stack_helper(0, None, 0)

    def _stack_helper(self, start, prev, cur_height):
        print("_stack_helper", start, prev, cur_height)
        if start >= self.n:
            # print("end", start, prev, cur_height)
            self.res = max(self.res, cur_height)
            return cur_height

        maximum = cur_height
        for i in range(start, self.n):
            # print("x", prev, start, i)
            if prev is None or self._is_stackable(i, prev):
                # print("stackable", prev, i, self.boxes[i][2])
                height = self.boxes[i][2]
                sub_res = self._stack_helper(i + 1, i, cur_height + height)
                maximum = max(sub_res, maximum)

        self.res = max(self.res, maximum)
        return maximum

    def _is_stackable(self, top, bottom):
        b = self.boxes
        return all([b[top][i] < b[bottom][i] for i in range(2)])

""" Solution 2: DP """
class Solution2:
    def __init__(self, boxes: List[List[int]]):
        self.boxes = sorted(boxes, key=lambda x: -x[0])
        self.n = len(self.boxes)

    def max_stack_height(self):
        dp = [x[2] for x in self.boxes]

        for i in range(self.n):
            _max = 0
            for j in range(i):
                # find the max
                if self._is_stackable(i, j):
                    _max = max(_max, dp[j])
            dp[i] += _max

        return max(dp)

    def _is_stackable(self, top, bottom):
        b = self.boxes
        return all([b[top][i] < b[bottom][i] for i in range(2)])

if __name__ == "__main__":
    # [W, D, H]
    boxes = [
        [3,9,9],
        [1,4,10],
        [5,10,11],
        [3,9,3],
        [1,5,3],
        [7,12,1]
    ]
    boxes = [
        [3,9,9],
        [4,8,8]
    ]
    obj = Solution2(boxes)
    print(obj.boxes)
    obj.max_stack_height()
    print(obj.max_stack_height())
    # print(obj)