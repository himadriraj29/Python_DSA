def trap(arr):
    n = len(arr)
    lmax = [-1 for i in range(n)]
    rmax = [-1 for i in range(n)]
    res = 0

    lmax[0] = arr[0]                                                      
    for i in range(1,n):
        lmax[i] = max(arr[i],lmax[i-1])

    rmax[n-1] = arr[n-1] 
    for i in range(n-2,-1,-1):
        rmax[i] = max(arr[i],rmax[i+1])

    for i in range(1,n-1):
        res += (min(lmax[i],rmax[i]) - arr[i])

    return res

arr = [5,0,6,2,3]
ans = trap(arr)
print(ans)