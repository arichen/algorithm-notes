# 78. Subsets
Link: https://leetcode.com/problems/subsets/

## Solution 1: iteration
Start with an empty subset, iteratively add elements to existing subsets to generate new subsets.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [x + [n] for x in res]
        return res
```

## Solution 2: backtrack