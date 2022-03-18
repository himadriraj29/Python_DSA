def naive(arr,l,r,p):
    A=[]
    idx=0
    for i in range(l,r+1):
        if arr[i]<arr[p]:
            A.append(arr[i])
            idx=idx+1
    for i in range(l,r+1):
        if arr[i]==arr[p]:
            A.append(arr[i])
            idx=idx+1
    for i in range(l,r+1):
        if arr[i]>arr[p]:
            A.append(arr[i])
            idx=idx+1
    print(A)
naive([5,3,8,1,10,2,4],0,6,6)
