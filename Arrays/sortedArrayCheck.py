def sortedArray(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr [i-1]:
            return False
    return True

arr = [45,76,90,100]
ans = sortedArray(arr)
print(ans)