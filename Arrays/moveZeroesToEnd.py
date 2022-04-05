def move(arr):
    n = len(arr)
    count =0
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[count]= arr[count], arr[i]
            count += 1
    return arr
arr = [100,0,99,0,12,0,6]
ans = move(arr)
print(ans)