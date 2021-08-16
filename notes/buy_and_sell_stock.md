# Buy and Sell Stock Problems

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
    - One transaction

- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
    - Unlimited transactions

- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
    - Two transactioins
    - Thoughts:
        1. Brute force: try each index to divide the array into left and right portion, find the max profit for each side. -> O(n^2)
            - what's duplicated: we keep recalculating the whole array as we increase/decrease the left right portion. e.g. a[0], a[0..1], a[0..2], a[0..3], the a[0] got recalculated many times.
            - how to optimize: if we know the min_price and max_profit up until a[i], we can immediately know the min_price and max_profit at a[j].
        2. DP from both directions. One keeps max a[0..i], one keeps max for a[i..n-1].
    - Thoughts 2:
        - subproblem: Sol(n) = max( best(:i) + best(i + 1:) for i in (0, n) ) => O(n) subproblems
        - pre-process best profit results with O(2n) = O(n) time, one pass from the left and one pass from the right


- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
    - k transactions
    - intuition: we know how to find best one transaction. after the 1st best transaction, we find the 2nd best. 3rd best, etc.
        - how: use a dp array to track "the best profit at index i for doing 1 trade". at the next iteration, we can build on it, a best profit at index i is: the best profit at index i - 1 from previous round, and possibly doing additional trade at index i.

- [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
    - unlimited transaction with cooldown time.
    - subproblem: dp(i) is the best profit of making a buy on day i
        - dp(i) = {(p[j] - p[i]) + max(dp(j + 2), dp(j + 3), ..., dp(n - 1)) for j in range(i + 1, n)}
    - original problem: max(dp)

# Thoughts:
- (Wrong!) The problem actually can convert to a maximum subarray problem.

    e.g. stock prices [3, 2, 6, 5, 0, 3] converts to profit array (compare with previous day) [0, 0, 4, -1, -5, 3]. and we are trying to find subarray with maxsum.

    1. one trade: find the max sum subarray.
    2. unlimited trades: collect all positive numbers.
    3. up to two trades: find up to top two sum subarrays.
    4. up to k trades: find up to top k sum subarrays.

    - what's wrong? e.g. `[1,2,4,2,5,7,2,4,9,0]`, two trades. It generates profit array `[3, 5, 7]`, which are (buy, sell): [(0, 2), (3, 5), (6, 8)], we will return max profit = 5 + 7 = 12 for max 2 trades. But max profit is [(0, 5), (6, 8)]. 6 + 7 = 13
    - not correct for one trade either.
    - correct for unlimited trades but there's no point to use it.

- maximum sequence? -> might be O(n ^ 2 * k)