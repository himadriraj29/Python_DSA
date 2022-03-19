def hoare(arr,l,r):
    il = l - 1
    ir = r + 1
    p = arr[l]
    while (True):
        il += 1
        while arr[il] < p:
            #arr[ir],arr[il] = arr[il],arr[ir]
            il += 1
        ir -= 1    
        while arr[ir] > p:
            ir -= 1
        if il >= ir:
            
            return ir       
        arr[ir],arr[il] = arr[il],arr[ir]

def quickSort(arr,l,r):
    if l < r:
        p=hoare(arr,l,r)
        quickSort(arr,l,p)
        quickSort(arr,p+1,r)

        
if __name__=="__main__":      
    A = [4,5,1,3,8,9,2,6]
    quickSort(A,0,7)
    print(A)