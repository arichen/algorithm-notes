class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

        # build segment tree
        self.build(arr)

    def build(self, arr):
        self.tree = [None] * self.n * 2
        self._build(0, 0, self.n - 1)

    def _build(self, index, start, end):
        if start == end:
            self.tree[index] = self.arr[start]
        else:
            mid = start + (end - start) // 2
            left = self._build(index * 2 + 1, start, mid)
            right = self._build(index * 2 + 2, mid + 1, end)
            self.tree[index] = left + right
        return self.tree[index]

    def update(self, index, val):
        self._update(0, index, val, 0, self.n - 1)

    def _update(self, cur_index, target, val, left, right):
        if left == right == target:
            diff = val - self.tree[cur_index]
            self.tree[cur_index] = val
            return diff

        mid = left + (right - left) // 2
        if target <= mid:
            # target at left child
            diff = self._update(cur_index * 2 + 1, target, val, left, mid)
        else:
            # target at right child
            diff = self._update(cur_index * 2 + 2, target, val, mid + 1, right)

        self.tree[cur_index] += diff
        return diff

if __name__ == "__main__":
    arr = [1,2,3]
    obj = SegmentTree(arr)
    print(obj.tree)

    obj.update(0,-1)
    obj.update(1,0)
    print(obj.tree)