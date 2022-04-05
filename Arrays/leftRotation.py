def rotate(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr
arr = [45,76,90,12,43]
ans = rotate(arr)
print(ans)

