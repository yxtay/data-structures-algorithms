def bubble_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr) - 1):
        swapped = False

        # Last i elements are already in place
        for j in range(0, len(arr) - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break


def selection_sort(arr):
    # i indicates how many items were sorted
    for i in range(len(arr) - 1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i + 1, len(arr) - 1):
            # Update the min_index if the element at j is lower than it
            if arr[j] < arr[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(arr):
    def merge(arr, left_arr, right_arr):
        i = j = k = 0

        # Copy data to temp arrays left_arr[] and right_arr[]
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_arr = arr[:mid]  # Dividing the array elements
        right_arr = arr[mid:]  # into 2 halves

        merge_sort(left_arr)  # Sorting the first half
        merge_sort(right_arr)  # Sorting the second half
        merge(arr, left_arr, right_arr)  # merge


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # element present at index number i

        j = i - 1
        while j >= 0 and key < arr[j]:  # comparing elements with the next until the last item
            arr[j + 1] = arr[j]
            j -= 1  # comparing each element to the elements present to its left
        arr[j + 1] = key  # new item becomes the key


def quick_sort(arr):
    def partition(array, low, high):
        # Select the pivot element
        pivot = array[high]
        i = low - 1

        # Put the elements smaller than pivot on the left and greater than pivot on the right of pivot
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort_rec(array, low, high):
        if low < high:
            # Select pivot position and put all the elements smaller than pivot on left and greater than pivot on right
            pi = partition(array, low, high)
            # Sort the elements on the left of pivot
            quick_sort_rec(array, low, pi - 1)
            # Sort the elements on the right of pivot
            quick_sort_rec(array, pi + 1, high)

    quick_sort_rec(arr, 0, len(arr) - 1)


def heap_sort(arr):
    def heapify(arr, n, i):
        # Find largest among root and children
        max_idx = i
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n and arr[max_idx] < arr[left_idx]:
            max_idx = left_idx

        if right_idx < n and arr[max_idx] < arr[right_idx]:
            max_idx = right_idx

        # If root is not largest, swap with largest and continue heapifying
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            heapify(arr, n, max_idx)

    # Build max heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        # swap largest to last
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)


def bucket_sort(arr):
    bucket = []

    for i in range(len(arr)):
        bucket.append([])

    for j in arr:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


def counting_sort(arr):
    output = [0] * len(arr)
    count = [0] * (max(arr) - min(0, *arr) + 1)

    for i, _ in enumerate(arr):
        count[arr[i]] += 1

    for i in range(min(0, *arr) + 1, max(arr) + 1):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i, el in enumerate(output):
        arr[i] = el


def radix_sort(arr):
    def counting_sort(arr, place):
        output = [0] * len(arr)
        count = [0] * 10

        for i in range(0, len(arr)):
            index = arr[i] // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // place
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:

        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2
