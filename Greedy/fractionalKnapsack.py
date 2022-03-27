def merge(arr1,arr2,arr3,l,r,mid):
    
    A = arr1[l:mid+1]
    B = arr1[mid+1:r+1]
    C = arr2[l:mid+1]
    D = arr2[mid+1:r+1]
    E = arr3[l:mid+1]
    F = arr3[mid+1:r+1]

    m = len(A)
    n = len(B)
    i = 0
    j = 0
    k = l

    while i<m and j<n:
        if A[i] < B[j]:
            arr1[k] = A[i]
            arr2[k] = C[i]
            arr3[k] = E[i]
            i += 1
            k += 1
        else:
            arr1[k] = B[j]
            arr2[k] = D[j]
            arr3[k] = F[j]
            j += 1
            k += 1
    while i<m:
        arr1[k] = A[i]
        arr2[k] = C[i]
        arr3[k] = E[i]
        i += 1
        k += 1
    while j<n:
        arr1[k] = B[j]
        arr2[k] = D[j]
        arr3[k] = F[j]
        j += 1
        k += 1

def merge_divide(arr1,arr2,arr3,l,r):
    
    if l < r:

        mid = (l + r)//2
        merge_divide(arr1,arr2,arr3,l,mid)
        merge_divide(arr1,arr2,arr3,mid+1,r)
        merge(arr1,arr2,arr3,l,r,mid)



def knapsack(arr1,arr2,arr3):    
    n = len(arr2)
    merge_divide(arr1,arr2,arr3,0,n)
    res = 0
    capacity = int(input())
    for i in range(n-1,-1,-1):
        if arr3[i] < capacity:
            res = res + arr2[i]
            capacity = capacity - arr3[i]
            i += 1
        else:
            res = res + capacity *(arr2[i]/arr3[i]) 
    return res

arr2 = [600,500,400]
arr3 = [50,20,30]
arr1 = []
for i in range(len(arr2)):
    arr1.append(arr2[i]/arr3[i])
res1 = knapsack(arr1,arr2,arr3)
print(res1)

    #merge_divide(arr1,arr2,arr3,0,n):


