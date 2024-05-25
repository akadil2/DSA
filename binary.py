def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return -1
# arr = [1,2,3,4,5,6]
# index = binary_search(arr,7)
# if index!=-1:
#     print(index)
# else:
#     print('not found')

def binary_search(arr, low, high, target):

    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return f"Found at {mid}"
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        else:
            return binary_search(arr, low, mid - 1, target)

    return -1


arr = [1,2,3,4,5,6]

index = binary_search(arr, 0, len(arr) - 1, 5)

print(index)

