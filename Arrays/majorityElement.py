#naive approach
def majority(arr):
    n = len(arr)
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                count += 1
        if count > n//2:
            return arr[i]
    return -1
arr = [5,6,6,5,6,7,8,6,6]
ans = majority(arr)
print(ans)