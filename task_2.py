def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1
    iter = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iter, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        iter += 1
    return (iter, arr[left])

arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.11]
target = 6.5
result = binary_search(arr, target)
print(result)