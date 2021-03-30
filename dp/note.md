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