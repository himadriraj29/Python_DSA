def maxSubArray(arr):
    maxi = arr[0]
    resi = arr[0]
    n = len(arr)
    for i in range(1,n):
        maxi = max(arr[i],maxi+arr[i])
        resi = max(maxi,resi)
    return resi

def maxCircleSubArray(arr):
    mini = arr[0]
    res = arr[0]
    sumi = 0
    maxsum = 0
    n = len(arr)
    for j in range(n):
        sumi += arr[j]

    for i in range(1,n):
        mini = min(arr[i],mini+arr[i])
        res = min(mini,res)
    maxsum = sumi-res
    return maxsum

arr = [1,3,-4,5,-6,8]
ans = max(maxSubArray(arr),maxCircleSubArray(arr))
print(ans)