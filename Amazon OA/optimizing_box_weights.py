from typing import List

def optimizing_box_weights(arr: List[int]) -> List[int]:
    arr = sorted(arr)
    n = len(arr)

    pre = arr[::]
    # calculate the prefix sum
    for i in range(1, n):
        pre[i] += pre[i - 1]

    # iterate from the largest item, stop when right partition > left partition
    i = n - 2
    while i >= 0 and pre[n - 1] - pre[i] <= pre[i]:
        i -= 1
    return arr[i + 1:]

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = optimizing_box_weights(arr)
    print(' '.join(map(str, res)))