from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def backtrack(path, arr):
            if not arr:
                self.res.append(path)
                return
            for i in range(len(arr)):
                backtrack(path + [arr[i]], arr[: i] + arr[i + 1:])

        backtrack([], nums)
        return self.res