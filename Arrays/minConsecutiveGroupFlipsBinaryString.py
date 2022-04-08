def flip(arr):
    n = len(arr)
    res = []
    j = 0
    for i in range(1,n):
        
        if arr[i] != arr[i-1]: 
                 
            if arr[i] != arr[0]: 
                res.append([])
                res[j].append(i)
            else:
                res[j].append(i-1)
                j += 1
        
    if arr[n-1] != arr[0]:
        res[j].append(n-1)
    j += 1

    return res
arr = [1,1,0,0,0,1,0,0,1,1,1,0,0,0]
ans = flip(arr)
print(ans)
