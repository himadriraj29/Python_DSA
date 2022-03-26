def lomuto(arr,l,r):
    p = r
    i = l - 1
    for j in range(l,r):
        if arr[j] <= arr[p]:
            i = i + 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[p] = arr[p],arr[i+1]
    print(arr)
lomuto([2,5,4,3,6,8,1,3,4],0,8)
        
    