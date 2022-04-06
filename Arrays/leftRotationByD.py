#method 1
'''
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
'''
#method 2
def rotate(arr,d):
    n = len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

def reverse(arr,low,high):
    while low < high:
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high -= 1

arr = [8,9,6,4,10,7]
d = 3
print(rotate([8,9,6,4,10,7],3))
