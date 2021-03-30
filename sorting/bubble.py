# algo: "sink" the largest item to the end
def bubble_sort(arr: list):
    if not arr:
        return

    n = len(arr)
    # for each loop for i, sink/push the largest item in a[:n - i] to the end
    for i in range(n - 1):
        # go through elements in range(0, n - i) and push larger item to the end
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # if want to bubble up smallest item to the front, go from the end to front

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
        bubble_sort(t)
        assert t == sorted(c)
