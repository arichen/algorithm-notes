# 115. Distinct Subsequences

## Approach 1: DFS + memoization

```python
class Solution:
@functools.cache
def numDistinct(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    if n == 0:
        return 1
    if m < n:
        return 0

    if s[0] == t[0]:
        return self.numDistinct(s[1:], t[1:]) + self.numDistinct(s[1:], t)
    else:
        return self.numDistinct(s[1:], t)
```

## Approach 2: DP

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # dp[0] is the number of distinct subsequence of s which equals ""
        for i in range(n + 1):
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
```