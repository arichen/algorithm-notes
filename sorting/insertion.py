# algo: iter through array and find correct position for each item
def insertion_sort(arr: list):
    if not arr:
        return

    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j] > arr[j - 1]:
                break
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

if __name__ == "__main__":
    cases = [
        [5,4,3,2,1],
        [3,4,2,1,3],
        [5,10,2],
        [3],
        [1,2,3,4,5]
    ]
    for c in cases:
        t = c[::]
        insertion_sort(t)
        assert t == sorted(c)
