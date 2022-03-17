
def merge(arr, l, m, r): 
    # code here
    #m=l+r//2
    A=[]
    idx1=l
    idx2=m+1
    
    #x=0
    
    while idx1<=m and idx2<=r:
        if arr[idx1]>arr[idx2]:
            A.append(arr[idx2])
            #x=x+1
            idx2=idx2+1
            #A[x]=arr[idx2]
        else:
            A.append(arr[idx1])
            #x=x+1
            idx1=idx1+1
            #A[x+1]=arr[idx1+1]
    
    while idx1<=m:
        A.append(arr[idx1])
        idx1=idx1+1
    while idx2<=r:
        A.append(arr[idx2])
        idx2=idx2+1
    j = 0  
    for i in range(l,r+1):
        arr[i] = A[j]
        j += 1
        
def mergeSort(arr, l, r):
    #code here
    if l>=r:
        return
    m=(l+r)//2
    mergeSort(arr,l,m)
    mergeSort(arr,m+1,r)
    merge(arr,l,m,r)


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    A=[5,6,2,3,1,9,4]
    mergeSort(A,0,6)
    print(A)