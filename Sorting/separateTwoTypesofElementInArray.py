def sepTwoEle(arr,l,r):
    p = 0
    i = l - 1
    for j in range(l,r+1):
        if arr[j] <= p:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    #p,arr[i+1] = arr[i+1],p
    return arr

arr = [1,0,1,0,1,0,0]
ans = sepTwoEle(arr,0,6)  
print(ans)