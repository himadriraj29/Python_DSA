def minDiffArray(arr):
    arr.sort()
    diff = float('inf')
    n = len(arr)
    for i in range(0,n-1):
        temp = arr[i+1] - arr[i]
        if temp < diff:
            diff = temp
    return diff

arr = [3,9,14,6]
ans = minDiffArray(arr)
print(ans)

