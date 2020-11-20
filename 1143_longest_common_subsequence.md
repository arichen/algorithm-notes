# 1143. Longest Common Subsequence

Thinking process:
1. DFS
starting from one string, iteratively matching each letter to the other string, recursively find the next matching letter.
=> time complexity: O(M * N * N)

2. DP
Working on subproblems and build up solution for the whole problem.
Use table to keep track of subproblem results.
To compare text1 = "abcde", text2 = "ace":
    1. (a, a): match, max_len = 1
    2. (a, ac): "a" != "c", take the max_len from previous step (a, a)
    3. (a, ace): "a" != "e", take the max_len from previous step (a, ac)
    4. (ab, a): "b" != "a", take the max_len from previous step (a, a)
    5. (abc, a): "c" != "a", take the max_len from previous step (a, a)
    ...
    6. (abc, ac): "c" == "c", take the max_len from without final character "c", (ab, c)

## notes
- Interesting idea to use `@functools.lru_cache` to cache the result of function call and aid dp.