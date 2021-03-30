https://leetcode.com/problems/minimum-knight-moves/

Keys:
- We only care about the absolute difference of target and starting point. consider only target's absolute value.
- target (x, y) is the same as target (y, x)

## Approach 1: one direction BFS
Keys:
- target (x, y) equals to target (abs(x), abs(y))
- keep a visited set to reduce explored starting point