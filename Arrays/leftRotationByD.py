def rotate(arr,d):
    n = len(arr)
    temp = []
    for i in range(0,d):
        temp.append(arr[i])
    for i in range(d,n):
        arr[i-d] = arr[i]
    for i in range(0,d):
        arr[n-d+i] = temp[i]
    return arr

arr = [8,9,6,4,10,7]
d = 3
print(rotate([8,9,6,4,10,7],3))