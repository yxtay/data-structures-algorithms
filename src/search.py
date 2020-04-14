def linear_search(arr, item):
    for i, el in enumerate(arr):
        if el == item:
            return i

    return -1


def ordered_linear_search(arr, item):
    for i, el in enumerate(arr):
        if el == item:
            return i
        elif el > item:
            return -1

    return -1


def binary_search_rec(arr, item):
    if not arr:  # list is empty -- our base case
        return -1

    midpoint = len(arr) // 2
    if arr[midpoint] == item:  # found it!
        return midpoint

    if item < arr[midpoint]:  # item is in the first half, if at all
        return binary_search_rec(arr[:midpoint], item)
    else:
        # otherwise item is in the second half, if at all
        result = binary_search_rec(arr[midpoint + 1 :], item)
        return (midpoint + result) if result >= 0 else -1


def binary_search_iter(arr, item):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == item:
            return middle

        if item < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1
