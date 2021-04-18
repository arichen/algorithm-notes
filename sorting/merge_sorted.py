# merge sorted array in-place
# A has enough space in the end to hold B
from typing import List

def merge(A: List[int], B: List[int], num_a: int):
    # since the extra space is in the end,
    # we merge from the end so there's no need to move elements back
    i, j = num_a - 1, len(B) - 1
    cur = len(A) - 1
    while i >= 0 and j >= 0:
        if A[i] >= B[j]:
            A[cur] = A[i]
            i, cur = i - 1, cur - 1
        else:
            A[cur] = B[j]
            j, cur = j - 1, cur - 1
    while j >= 0:
        A[cur] = B[j]
        cur, j = cur - 1, j - 1

if __name__ == "__main__":
    A = [2,4,6,8,10]
    B = [1,3]
    res = A + [0] * len(B)
    merge(res, B, len(A))
    print(res)