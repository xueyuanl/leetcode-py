def binary_search(arr, target, l=0, r=None):
    left = l
    right = r if r is not None else len(arr) - 1

    while left <= right:
        mid = left + (right - left) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return None
