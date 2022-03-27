def merge(arr,l,r,mid):
    A = arr[l:mid+1]
    B = arr[mid+1:r+1]
    m = len(A)
    n = len(B)
    i = 0
    j = 0
    k = l

    while i<m and j<n:
        if A[i][0] < B[j][0]:
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

'''
def mergeOverlapIntervals(arr):
    res = 0
    n = len(arr)
    merge_divide(arr,0,n)
    for i in range(1,n):
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1],arr[i][1])
            arr[res][0] = min(arr[res][0],arr[i][0])
            
        else:
            res += 1
            arr[res] = arr[i]
            
        i += 1
    return res
'''
def mergeOverlapIntervals(arr):
    arry = []
    res = 0
    n = len(arr)
    merge_divide(arr,0,n)
    arry.append(arr[res])
    for i in range(1,n):
        if arry[-1][1] >= arr[i][0]:
            arry[-1][1] = max(arry[-1][1],arr[i][1])
            arry[-1][0] = min(arry[-1][0],arr[i][0])
            
        else:
            res += 1
            arry.append(arr[i])
            
        i += 1
    return arry

arr = [[2,4],[1,3],[8,10],[5,7],[6,9]]
ans = mergeOverlapIntervals(arr)
print(ans)
