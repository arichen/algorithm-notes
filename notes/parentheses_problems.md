# Parentheses Problems

## Basic
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Twist
- [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)
    - thoughts: what's different than basic parentheses check problem?
        -> alphanumeric chars to ignore. without these, we just push parenthesis to stack
        -> we only need left parentheses in stack
        -> we only need index of left parentheses in stack!
- [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
    - Thoughts:
        1. Tick the counter everytime seeing an imbalance.
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
    - Thoughts:
        1. Brute Force: try remove/keep every spot
        2. Optimize brute force: first calculate the minimum number of removals for left and right bracket. And dfs to try possibilities out.

## Wildcard
- [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)
    - Approach 1: DFS (TLE)
        - For each "*", dfs all possibilities.
    - Approach 2: Greedy
        - Modify the use of balance counter.
    - Approach 3: DP
        - Subproblem: A[i...j] is valid if
            - A[j] = "*" and A[i...j-1] is valid
            - A[j] can be made to ")" and there's an A[k] can be made to "(" such that A[i..k-1] and A[k+1..j-1] are both valid.

## Generate all valid parentheses
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
    - Thoughts:
        1. first thought is to use python's itertools.permutations. But it will have duplicates. -> can use set, but redudant. -> O(n!)
        2. backtrack, iterate through the decision tree. for each spot, is it a valid spot for left bracket? is it a valid spot for right bracket?

## Substring
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
    - Thoughts:
        1. Use balance count. Everytime sees a valid pair, add 2 to the result. -> problem: need to be substring. meaning need to be consecutive. e.g. "()(()" will return 4, correct ans is 2.
        2. Modified use of balance count. Add a global max and current count.
        2. Use stack -> still, how to only count the consecutive string and "concat" two valid parentheses together? e.g. Handle difference of "()()" and "()(()".
            - -> use index
            - the bottom of stack is the "wall" or "separator". It's the index of where a new valid substring can start. e.g. bottom of stack is -1, meaning a valid substring can start at index 0.
            - the rest of stack is the index of left bracket.
            - If in stack there's only "wall" (only one item in stack), that means there's no left bracket available, the new wall should be the current index.


## Thoughts
- When to use stack? When to just use balance counter? -> use counter when we only need to verify the simple balanceness. use stack when condition is more complicated. (multiple pairs e.g.(){}[]., need to output other characters within string)
- When simple stack is not enough, can index help?