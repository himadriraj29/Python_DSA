def count_inv(arr,l,r):
    res = 0
    if l < r:
        
        mid =  (l + r) // 2
        res += count_inv(arr,l,mid)
        res += count_inv(arr,mid+1,r)
        res += merge(arr,l,r,mid)
    return res

def merge(arr,l,r,mid):
    A = arr[l : mid + 1]
    B = arr[mid+1 : r + 1]
    i = 0
    j = 0
    k = l
    count = 0
    m = len(A)
    n = len(B)
    while i < m and j < n:
        if A[i] < B[j]:
            arr[k] = A[i]
            k += 1
            i += 1
        else:
            arr[k] = B[j]
            k += 1
            j += 1
            count += m-i
    while i < m:
        arr[k] = A[i]
        k += 1
        i += 1
    while j < n:
        arr[k] = B[j]
        k += 1
        j += 1
    return count
arr = [4,3,2,1,5,7,6]
a = count_inv(arr,0,6)
print(a)





   

        
