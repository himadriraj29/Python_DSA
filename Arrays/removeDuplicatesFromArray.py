def duplicates(arr):
    res = 1
    n = len(arr)
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            res = res
        else:
            res += 1
    return res
arr = [45,76,90,100]
ans = duplicates(arr)
print(ans)