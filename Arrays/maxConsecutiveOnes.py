def consecOnes(arr):
    res = 0
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            res = max(res,count)
    return res

arr = [1,1,0,0,1,1,1,1,0,1,0]
ans = consecOnes(arr)
print(ans)