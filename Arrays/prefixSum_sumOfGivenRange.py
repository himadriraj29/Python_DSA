def prefixSumRange(arr,l,r):
    n = len(arr)
    res = 0
    for i in range(1,n):
        arr[i] = arr[i] + arr[i-1]
    res = arr[r] - arr[l-1]
    return res
    

arr = [2,3,4,1,5,4,3]
ans = prefixSumRange(arr,3,5)
print(ans)
