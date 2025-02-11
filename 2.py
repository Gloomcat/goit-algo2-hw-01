from random import randint, randrange
from typing import List

def k_min_select(arr: List[int], k: int) -> int | None:
    if not arr or k < 0 or k >= len(arr):
        return None

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left, mid, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            mid.append(x)
        else:
            right.append(x)

    if k < len(left):
        return k_min_select(left, k)
    elif k < len(left) + len(mid):
        return pivot
    else:
        return k_min_select(right, k - len(left) - len(mid))


if __name__ == "__main__":
    size = 100
    arr = [randrange(-1000, 1000) for _ in range(size)]
    print("arr:", arr)
    k = randint(0, size - 1)
    print(f"k-th ({k}) min value:", k_min_select(arr, k))
    print(f"k-th ({k}) min value, verification:", sorted(arr)[k])
