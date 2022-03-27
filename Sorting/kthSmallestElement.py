def lomuto(arr,l,r):
    p = r
    i = l - 1
    for j in range(l,r):
        if arr[j] <= arr[p]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[p],arr[i+1] = arr[i+1],arr[p]
    return i+1

def kthSmallest(arr,k):
    n = len(arr)
    l = 0
    r = n - 1
    while l < r:
        idx = lomuto(arr,l,r)
        if idx == k - 1:
            return arr[idx]
        if idx < k - 1:
            l = idx + 1
        else:
            r = idx - 1
    return -1

arr = [4,7,3,1,6,5]
ans = kthSmallest(arr,3)  
print(ans) 
