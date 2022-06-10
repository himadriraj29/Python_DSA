#using memoization
def fiboDPmemo(n):
    memo = [-1 for i in range(n+1)]
    if memo[n] == -1:
        res = 0
        if n == 0 or n == 1:
            res = n
        else:
            res = fiboDPmemo(n-1) + fiboDPmemo(n-2)
        memo[n] = res
    return memo[n]

#using tabulation
def fiboDPtabu(n):
    tabu = []
    #tabu = [-1 for i in range(n+1)] 
    tabu.append(0)
    tabu.append(1)
    for i in range(2,n+1):
        tabu.append(tabu[i-1] + tabu[i-2]) 
    return tabu[n]

n = 9
#ans = fiboDPmemo(n)
ans = fiboDPtabu(n)
print(ans)
