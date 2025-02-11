from random import randrange
from typing import List, Tuple


def find_min_max(
    left: Tuple[int, int] | None, right: Tuple[int, int] | None
) -> Tuple[int, int]:
    if not left:
        return right
    if not right:
        return left

    min_val = left[0] if left[0] <= right[0] else right[0]
    max_val = left[1] if left[1] >= right[1] else right[1]
    return min_val, max_val


def split_find_min_max(arr: List[int]) -> Tuple[int, int] | None:
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    return find_min_max(split_find_min_max(arr[:mid]), split_find_min_max(arr[mid:]))


if __name__ == "__main__":
    arr = [randrange(-1000, 1000) for _ in range(100)]
    print("(arr):", arr)
    print("(min, max):", split_find_min_max(arr))
    print("(min, max) verification:", (min(arr), max(arr)))
