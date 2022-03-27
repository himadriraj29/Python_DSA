def chocolate(arr,m):
    arr.sort()
    n = len(arr)
    mini = float('inf')
    for i in range(n-m+1):
        temp = arr[i + m -1] - arr[i]
        if temp < mini:
            mini = temp
        
    return mini
arr = [2,4,7,10,8,3,5]  
ans = chocolate(arr,3)
print(ans)



