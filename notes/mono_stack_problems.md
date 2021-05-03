# Mono Stack Problems

- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
    1. Thought 1:
        - Brute force: for each bar, find the first bars to the left and right that are shorter than current bar, the area this bar can make is bar_height * (right - left - 1). -> O(n^2)
        - Base on this idea, use two mono increasing stack to track left and right bounds separately. After we have the left and right bound, aka a bar's lower bound and higher bound, we can calculate the max area a bar can "grow" to is bar_height * (right - left - 1) -> O(3 * n) = O(n)
    2. Thought 2: another brute force idea: try each (left, right) range pair as area width, and use the minimum height in each range as its area height. -> O(n ^ 2)
    3. Thought 3: taking the intuition of thought 1, can we do it in one iteration?
        - Idea is to find the left-most and right-most bound for each bar.
        - The bound on both sides are the first bar that is shorter than current one.

        Method:
        1. Use a stack to keep track of all bars that haven't found right bound.
        2. Add bars in ascending order, which means the lower bar is always the upper bar's left bound. When a bar is the last item in stack, that means there is no left bound, it can go all the way to the left.
        3. When current bar is shorter than the top bar in stack, that means we found the right bound. Process bars in stack until top bar is shorter than current bar, then push current bar on to stack.

- [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
    1. Thought process:
        1. The DP idea for finding maximal square? But not working for rectangle
        2. How do we brute force it? Dfs? not working.
        3. What is the property of a rectangle? Width and height. What determines the max width and height of a rectangle ending at `m[i][j]`? -> a relation to the histogram problem.
