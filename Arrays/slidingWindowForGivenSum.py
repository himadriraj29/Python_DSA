def windowSum(arr, sumi):
    n = len(arr)
    currsum = arr[0]
    start = 0
    for end in range(1,n):
        while currsum > sumi and start < end-1:
            currsum -= arr[start]
            start += 1
        if currsum == sumi:
            return True
        if end < n:
            currsum += arr[end]
    return currsum == sum

arr = [2,3,1,4,6,2]
ans = windowSum(arr, 8)
print(ans)
                
    