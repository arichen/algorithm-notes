# binary search: left < right
# condition: we want to find the boundary of left and right sections
# search space: [left, right)
# when left == right, it means we find the boundary of left and right section.
# left section: A[:left]; right section: A[right:]

# array: [T, T, T, .., F, F, ...] return the first index that's False
def search(array):
    n = len(array)

    # [left, right) is the search space
    # for all right <= i < n, arr[i] is False
    left, right = 0, n

    # since right indicates known smallest index that's False,
    # when left == right, left is the first index in array to be False
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == False:
            right = mid
        else:
            left = mid + 1

    return left if left < n else -1

if __name__ == "__main__":
    arr = [False]
    res = search(arr)
    print(res)