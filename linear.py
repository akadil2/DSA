def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1


arr = [13,32,43,48,51,56]
index = linear_search(arr, 51)

if index != -1:
    print(index)
else:
    print("Not Found")

