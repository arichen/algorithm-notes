# Binary Search

- left <= right
    - Search for exact value
    - `<=` searches for every element

- left < right
    - Search for bound that split the data in two sections
    - When looking for left bound, use `right` as the potential answer (spliting point) once `left` meets it.
    - When looking for right bound, use `left` as the potential answer once `right` meets it.


### 162. Find Peak Element
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # finding a local max
        # intuition: look to the side that's increasing, until it's not
        # => finding the right bound of an increasing range
        # loop condition: left < right
        # left: largest index of increasing part
        #
        # or, can also think this way
        # => find the left bound of an decreasing range (increasing from right to left)
        # right: smallest index of decreasing part

        n = len(nums)
        if n == 1:
            return 0

        low, high = 0, n - 1
        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low
```