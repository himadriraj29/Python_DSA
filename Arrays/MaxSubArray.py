def maxSubArray(arr):
    maxi = arr[0]
    res = arr[0]
    n = len(arr)
    for i in range(1,n):
        maxi = max(arr[i],maxi+arr[i])
        res = max(maxi,res)
    return res
arr = [1,3,-4,5,-6,8]
ans = maxSubArray(arr)
print(ans)