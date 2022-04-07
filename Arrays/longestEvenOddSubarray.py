def evenodd(arr):
    n = len(arr)
    count = 1
    res = 1
    for i in range(1,n):
        if (arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
            count += 1
            res = max(count,res)
        else:
            count = 1
    return res

arr = [5,10,20,6,3,8]
ans = evenodd(arr)
print(ans)
            
