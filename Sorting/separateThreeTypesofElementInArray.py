def sepThreeEle(arr,l,r,mid):
    n = len(arr)
    l = 0
    r = n - 1
    mid = 0
    while mid<r:
        if arr[mid] < 1:
            arr[l],arr[mid] = arr[mid],arr[l]
            mid += 1
            l += 1
    
        elif arr[mid]  == 1:
            mid += 1
    
        elif arr[mid] > 1:
            arr[r],arr[mid] = arr[mid],arr[r]
            r -= 1    
    return arr

arr = [1,2,1,0,2,1,0]
ans = sepThreeEle(arr,0,6,0)  
print(ans)