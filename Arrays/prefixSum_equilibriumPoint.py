def equilibrium(arr):
    sumi = 0
    lsum = 0
    rsum = 0
    n = len(arr)
    for i in range(n):
        sumi += arr[i]
    for i in range(n):
        if lsum == sumi - arr[i]:
            return True
        lsum += arr[i]
        sumi -= arr[i]
    return False

arr = [2,3,2]
ans = equilibrium(arr)
print(ans)


