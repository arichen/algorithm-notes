# Binary Search

- left <= right
    - Search for exact value
    - `<=` searches for every element

- left < right
    - Split the array into two sections
    - When looking for the first element in the second partition
        - using `left` to approach `right`. `right` is the first element in the second partition.
        - `mid = left + (right - left) // 2`
        - `left = mid + 1`, if mid belongs to the first partition
        - `right = mid`, if mid belongs to the second partition

    - When looking for the last element in the first partition
        - using `right` to approach `left`. `left` is the last element in the first partition.
        - `mid = left + (right - left) // 2 + 1`. "+1" to let mid lean toward right.
        - `left = mid`, if mid belongs to the first partition
        - `right = mid - 1`, mid belongs to the second partition

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