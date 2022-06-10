def fiboDP(n):
    memo = [-1 for i in range(n+1)]
    if memo[n] == -1:
        res = 0
        if n == 0 or n == 1:
            res = n
        else:
            res = fiboDP(n-1) + fiboDP(n-2)
        memo[n] = res
    return memo[n]
    

n = 9
ans = fiboDP(n)
print(ans)
