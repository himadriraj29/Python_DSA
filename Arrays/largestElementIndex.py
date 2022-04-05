def largestIndex(arr):
    res = 0
    n = len(arr)
    for i in range(n):
        if arr[i-1] > arr[i]:
            res = i-1
    return res

arr = [45,76,90,12,43]
ans = largestIndex(arr)
print(ans)

    