def maxSubArray(arr):
    maxi = arr[0]
    res = arr[0]
    n = len(arr)
    for i in range(1,n):
        maxi = max(arr[i],maxi+arr[i])
        res = max(maxi,res)
    return res
arr = [-100,-200,-300]
ans = maxSubArray(arr)
print(ans)