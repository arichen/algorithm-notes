# Coin Change Problems

- [322. Coin Change](https://leetcode.com/problems/coin-change/)
    - intuition: to add coin C to the pile and make total value V, the pile has value V-C before adding coin.

- [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)
    - thoughts (wrong): define dp[i] as the number of combinations to make value i. Then use the dp value in dp[v-c] for each coin and sum them together -> duplicate. e.g. 2 + 1 is the same as 1 + 2.
        - what's duplicated? -> if we iterate by total value and by coin type as in 1st problem, we can go into the 2+1 and 1+2 problem. but what if we do by each coin and then by each value?
    - DP: iterate through each coin face value. for each total amount value `v`, the total number of combination is the number of combinations to make `v` with coin[0...i-1], plus the number of combinations to make `v - coin[i]` with coin[0...i].
    ```
        0 <= i < length of coins; 1 <= j <= amount
        dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i]]
    ```
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]
```