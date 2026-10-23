
# algorithms/sorting.py


def bubble_sort(arr):
    nums = arr.copy()
    n = len(nums)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums


def selection_sort(arr):
    nums = arr.copy()
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


def insertion_sort(arr):
    nums = arr.copy()

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


def heap_sort(arr):
    nums = arr.copy()
    n = len(nums)

    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and nums[left] > nums[largest]:
            largest = left

        if right < size and nums[right] > nums[largest]:
            largest = right

        if largest != root:
            nums[root], nums[largest] = (
                nums[largest], nums[root]
            )
            heapify(size, largest)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Move largest elements to the end
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(i, 0)

    return nums


if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 3]

    print("Original: ", numbers)
    print("Bubble:   ", bubble_sort(numbers))
    print("Selection:", selection_sort(numbers))
    print("Insertion:", insertion_sort(numbers))
    print("Merge:    ", merge_sort(numbers))
    print("Quick:    ", quick_sort(numbers))
    print("Heap:     ", heap_sort(numbers))
