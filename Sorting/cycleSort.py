def cycle(arr):
    n = len(arr)
    
    for i in range(n):
        count = i
        elm = arr[i]
        for j in range(i+1, n):
            if arr[j] < elm:
                count += 1
        arr[count],elm=elm,arr[count]
        while count != i:
            count = i
            for j in range(i+1, n):
                if arr[j] < elm:
                    count += 1
            arr[count],elm=elm,arr[count]

arr = [7, 11, 2, 4]
cycle(arr)
print(arr)