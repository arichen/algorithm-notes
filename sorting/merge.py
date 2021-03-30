# algo
# 1. divide array in the middle to left and right
# 2. recursive merge sort left and right array
# 3. merge left and right as merging two sorted arrays. O(n)
class MergeSort:
    def __init__(self):
        pass

    def merge(self, arr, left, middle, right):
        res = []
        i, j = left, middle
        while i < middle and j <= right:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        if i < middle:
            res += arr[i: middle]
        if j <= right:
            res += arr[j: right + 1]
        arr[left: right + 1] = res

    def sort(self, arr: list, left: int, right: int):
        # sorting arr[left: right + 1]
        # stop when input has only 1 item or empty
        if not arr or (right - left) < 1:
            return

        # we need to divide the input array to 2
        # +1 to make sure the middle is at the second element if array size is 2
        middle = left + (right - left + 1) // 2
        self.sort(arr, left, middle - 1)
        self.sort(arr, middle, right)
        self.merge(arr, left, middle, right)


if __name__ == "__main__":
    # merge test cases
    if False:
        cases = [
            ([1,4,2,3], 0, 2, 3),
            ([1,2,3,4], 0, 3, 3),
            ([1,2,3,4], 0, 4, 4),
            ([1,2,3,4,5,6], 0, 2, 5)
        ]
        for c, l, m, r in cases:
            t = c[::]
            MergeSort().merge(t, 0, 2, 3)
            assert t == sorted(c)
    # exit()

    # sort test cases
    cases = [
        [5,4,3,2,1],
        [3,4,2,1,3],
        [5,10,2],
        [3],
        [1,2,3,4,5]
    ]
    for c in cases:
        t = c[::]
        MergeSort().sort(t, 0, len(t) - 1)
        assert t == sorted(c)