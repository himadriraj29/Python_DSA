def prefixSum(arr):
    n = len(arr)
    for i in range(1,n):
        arr[i] = arr[i] + arr[i-1]
    return arr

arr = [2,3,4,1]
ans = prefixSum(arr)
print(ans)
