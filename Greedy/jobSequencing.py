def merge(arr1,arr2,l,r,mid):
    
    A = arr1[l:mid+1]
    B = arr1[mid+1:r+1]
    C = arr2[l:mid+1]
    D = arr2[mid+1:r+1]

    m = len(A)
    n = len(B)
    i = 0
    j = 0
    k = l

    while i<m and j<n:
        if A[i] < B[j]:
            arr1[k] = A[i]
            arr2[k] = C[i]
            i += 1
            k += 1
        else:
            arr1[k] = B[j]
            arr2[k] = D[j]
            j += 1
            k += 1
    while i<m:
        arr1[k] = A[i]
        arr2[k] = C[i]
        i += 1
        k += 1
    while j<n:
        arr1[k] = B[j]
        arr2[k] = D[j]
        j += 1
        k += 1

def merge_divide(arr1,arr2,l,r):
    
    if l < r:

        mid = (l + r)//2
        merge_divide(arr1,arr2,l,mid)
        merge_divide(arr1,arr2,mid+1,r)
        merge(arr1,arr2,l,r,mid)

def jobSequence(arr1,arr2):
    n = len(arr1)
    sum = 0
    merge_divide(arr1,arr2,0,n)
    maxi = max(arr2)
    res = [-1 for i in range(maxi)]
    profit = 0
    for i in range(n-1,-1,-1):
        slot = arr2[i] - 1
        while slot >= 0 and res[slot] != -1:
            slot -= 1
        if slot != -1:
            res[slot] = i
            profit += arr1[i]
    return profit



#arr1 == profit
#arr2 == deadline

arr1 = [100,50,10,20,30]
arr2 = [2,1,2,1,3]
ans = jobSequence(arr1,arr2)
print(ans)

