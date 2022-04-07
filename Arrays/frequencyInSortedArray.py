def frequency(arr):
    n = len(arr)
    freq = 1
    i = 1
    j = 0 
    res = []
    while i < n:
        while i < n and arr[i] == arr[i-1]:
            freq += 1
            i += 1
        res.append([])
        res[j].append(arr[i-1])
        res[j].append(freq)
        j += 1
        i += 1
        freq = 1
    
    if n == 1 or arr[n-1] != arr[n-2]:
        res.append([])
        res[j].append(arr[n-1])
        res[j].append(1)
    return res

arr = [45,45,45,33,33,21]
ans = frequency(arr)
print(ans)


