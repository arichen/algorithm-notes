- subproblem: dp[i:j] is whether s[i:j] is palindromic => O(n^2) subproblems
    dp[i:j] = True, if s[i] == s[j] and dp[i+1:j-1]
    dp[i:j] = False, else
- each subproblem takes O(1) time to solve