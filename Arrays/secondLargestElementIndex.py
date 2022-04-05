def SeclargestIndex(arr):
    res = -1
    largest = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[largest]:
            res = largest
            largest = i
        elif arr[i] != largest:
            if arr[i] > arr[res] or res == -1:
                res = i
    return res

arr = [45,76,90,12,43]
ans = SeclargestIndex(arr)
print(ans)

    