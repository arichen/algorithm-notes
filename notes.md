# Binary Tree
- Use array to store binary tree.
    - If index starts from 0, object at ith index's children: (2i + 1, 2i + 2)
    - If index starts from 1, object at ith index's children: (2i, 2i + 1)

# Heap
- In a binary min heap, the maximum element can be found in O(N)
    - doesn't use the property of min heap, simply traversing all the nodes

- In python heapq library, pop method returns the min.

# Recursion
- when drill down to subproblem, mind the grouping. Is the grouping complete exhaustive?
    - e.g. Ways to put parenthesis `"1+2*3-4"`. my first intuition is take the first element and recur the rest, plus take the first two element and recur the rest. But it's not correct, it won't cover the case `"(1+2*3)-4"`.

# DP
## Condition
1. Problem has optimal substructure: optimal solution can be constructed from optimal solutions from subproblems.
2. The subproblem overlap.

## Two ways of DP
1. Top-down: DFS + memoization
2. Bottom-up: solve subproblems first and build up to the final solution. Usually tabular form.

## Compare the two ways of DP
### Top-down pros:
1. The order/sequence of solving subproblem doesn't matter. Recurssion and memoization takes care of sobproblems.
2. Easier to reason for partition type of problems (how many ways are there to..., splitting a string into...)

### Bottom-up pros:
1. Easier to reason the time complexity.
2. No recursion. No concern about stack overflow.