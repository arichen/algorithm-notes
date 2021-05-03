# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

- Thought process:
    - How I would do it by hand? Horizontal cuts generate slice heights, and vertical cuts generates widths. The max area is produced by the max of heights and widths.
    - iterate through array and find diff -> the array was not ordered -> sort takes O(nlogn) -> iterate through 1 to W/H and see if its a cut -> too slow, in test cases W/H is way larger than n -> sort array.

```python
class Solution:
    def getMaxSlice(self, length: int, cuts: List[int]) -> List[int]:
        res, last = 0, 0
        for c in cuts:
            res = max(res, c - last)
            last = c
        return max(res, length - last)

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_height = self.getMaxSlice(h, sorted(horizontalCuts))
        max_width = self.getMaxSlice(w, sorted(verticalCuts))
        return max_height * max_width % (10 ** 9 + 7)
```