'''mini = float("-inf")
if -10000000 > mini:
    print("s")
    '''
def select(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[mini]>arr[j]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    print(arr)
select([3,1,8,2])
                