def hoare(arr,l,r):
    il = l - 1
    ir = r + 1
    p = arr[l]
    while (True):
        il += 1
        while arr[il] < p:
            il += 1
        ir -= 1
        while (arr[ir] > p):
            ir -= 1
        if il >= ir:
            print(arr)
            return ir
        arr[il],arr[ir]=arr[ir],arr[il]

hoare([4,5,3,2,6,1],0,5)
