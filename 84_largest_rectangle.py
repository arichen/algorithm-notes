# Algorithm
# Idea is to find the left-most and right-most bound for each bar.
# The bound on both sides are the first bar that is shorter than current one.
#
# Method:
# 1. Use a stack to keep track of all bars that haven't found right bound.
# 2. Add bars in ascending order, which means the lower bar is always the upper bar's left bound. When a bar is the last item in stack, that means there is no left bound, it can go all the way to the left.
# 3. When current bar is shorter than the top bar in stack, that means we found the right bound. Process bars in stack until top bar is shorter than current bar, then push current bar on to stack.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = []
        max_area = 0
        heights.append(0)
        # add an ending element to push out all remaining bars in stack

        for i, v in enumerate(heights):
            while stack and v < heights[stack[-1]]:
                # current bar is shorter than the top bar in stack, right bound of top bar found
                idx = stack.pop()
                width = (i - stack[-1] - 1) if stack else i
                max_area = max(width * heights[idx], max_area)
            stack.append(i)

        return max_area