# Subsequence Problems

- [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)
    - thought: simply compare two string one index by one index, and see if all indices of s were matched.

- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)
    - Given two strings s and t, return the number of distinct subsequences of s which equals t.
    - Thought: use the same intuition as the 392. everytime we see a match, we can either use this index or not use it. -> DFS + memoization
    - DP
        ```
        f(s[0..i], t[0..t]) =
            if s[i] == t[j], f(s[0...i-1], t[0...t-1]) + f(s[0...i], t[0...t-1])
            else, f(s[0...i], t[0...t-1])
        ```

- [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)
    - Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
    1. naive: iterate through `words`, check if `words[i]` is subsequence of s one by one. -> O(len(words) * len(s)) -> might have too many duplicated work.
    2. build `words` as trie, and iterate through `s` and check if there is matching entry in trie. -> trie has problem handling..
    3. go back to the idea in 392. All we need to determine whether a subsequence exist is whether characters appear in certain sequence. We have one target character at a time. -> use a dictionary to keep all the next target characters and their respective following sequences. e.g. `["a", "bb", "acb", "ade"]`, we have dict `{"a": ["", "cb", "de"], "b": ["b"]}`, if we see `"a"`, then pop out key a, and we know we've found 1 complete sequence (empty string met), and we need to look for `"c"` and `"d"` the next.