def intersect(arr1,arr2):
    arr3 = []
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    while i<m and j<n:
        if i>0 and arr1[i]==arr1[i-1]:
            i += 1
            continue
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            arr3.append(arr1[i])
            i += 1
            j += 1
    print(arr3)
intersect([4,6,7,9,10],[4,7,8,9,11])
