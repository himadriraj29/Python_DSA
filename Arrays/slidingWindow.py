def window(arr,k):
    currsum = 0
    maxsum = 0
    n = len(arr)
    for i in range(k):
        currsum += arr[i] 
        maxsum = currsum
    for j in range(n):
        currsum += arr[j] - arr[j-k]
        maxsum = max(currsum, maxsum)
    return maxsum
arr = [45,45,45,33,33,21]
ans = window(arr,3)
print(ans)























