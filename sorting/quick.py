def quick_sort(arr: list, left: int, right: int):
    if not arr or right <= left:
        return

    p = left
    i, j = left + 1, right + 1
    while i < j:
        if arr[i] > arr[p]:
            j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    arr[p], arr[i - 1] = arr[i - 1], arr[p]
    p = i - 1

    quick_sort(arr, left, p - 1)
    quick_sort(arr, p + 1, right)


if __name__ == "__main__":
    cases = [
        [5,4,3,2,1],
        [3,4,2,1,3],
        [5,10,2],
        [3],
        [1,2,3,4,5],
        [2,1,4,3,6]
    ]
    for c in cases:
        t = c[::]
        quick_sort(t, 0, len(t) - 1)
        assert t == sorted(c)
