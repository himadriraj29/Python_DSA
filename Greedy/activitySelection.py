
def merge(arr,l,r,mid):
    A = arr[l:mid+1]
    B = arr[mid+1:r+1]
    m = len(A)
    n = len(B)
    i = 0
    j = 0
    k = l

    while i<m and j<n:
        if A[i][1] < B[j][1]:
            arr[k] = A[i]
            i += 1
            k += 1
        else:
            arr[k] = B[j]
            j += 1
            k += 1
    while i<m:
        arr[k] = A[i]
        i += 1
        k += 1
    while j<n:
        arr[k] = B[j]
        j += 1
        k += 1

def merge_divide(arr,l,r):
    
    if l < r:
        mid = (l + r)//2
        merge_divide(arr,l,mid)
        merge_divide(arr,mid+1,r)
        merge(arr,l,r,mid)

def activitySelector(arr):
    n = len(arr)
    merge_divide(arr, 0, n)
    listi = []
    listi.append(arr[0])
    for i in range(1,n):
        if  listi[-1][1] <= arr[i][0]:
            listi.append(arr[i])
    return listi

arr = [(4,6),(3,5),(5,8),(1,3),(6,9)]
ans = activitySelector(arr)
print(ans)



