def lomuto(arr,l,r):
    i = l - 1
    p = r
    for j in range(l,r):
        if arr[j] < arr[p]:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[p] = arr[p],arr[i+1]
    return i+1

def quickSort(arr,l,r):
    if l < r:
        p=lomuto(arr,l,r)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,r)

if __name__=="__main__":      
    A = [4,5,1,3,8,9,2,6]
    quickSort(A,0,7)
    print(A)
        

