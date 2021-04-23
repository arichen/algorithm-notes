# 309. Best Time to Buy and Sell Stock with Cooldown

## Approach 1: DFS + memoization (TLE)

```python
class Solution:
    @functools.cache
    def helper(self, prices: tuple) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if n == 2:
            return max(prices[1] - prices[0], 0)

        lowest, res = prices[0], 0
        for i in range(1, n):
            if prices[i] > lowest:
                res = max(res, prices[i] - lowest + self.maxProfit(prices[i + 2:]))
            else:
                lowest = prices[i]
        return res

    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(tuple(prices))
```
