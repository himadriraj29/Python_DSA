def stock(arr):
    profit = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[i-1]:
            profit += (arr[i] - arr[i-1])
    return profit

arr = [1,5,3,8,12]
ans = stock(arr)
print(ans)