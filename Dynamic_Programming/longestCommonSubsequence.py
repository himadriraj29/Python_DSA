
#lcs without dp: using recursion
def lcs(s1,s2,i,j):
    if i == 0 or j == 0:
        return 0
    elif s1[i] == s2[j]:
        return 1 + lcs(s1,s2,i-1,j-1)
    else:
        return max(lcs(s1,s2,i,j-1), lcs(s1,s2,i-1,j))

#lcs using dp: memoiztion
def lcsM(s1,s2,i,j,memo):
    
    if i == 0 or j == 0:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    if s1[i-1] == s2[j-1]:
        memo[i][j] = 1 + lcsM(s1,s2,i-1,j-1,memo)
        return memo[i][j]
   
    memo[i][j] = max(lcsM(s1,s2,i,j-1,memo), lcsM(s1,s2,i-1,j,memo))
    return memo[i][j]


s1 = 'himadriraj'
s2 = 'mitaliraj'
i = len(s1)
j = len(s2)
memo = [[-1 for k in range(j+1)] for l in range(i+1)]
#print(lcs(s1,s2,9,8))
print(lcsM(s1,s2,i,j,memo))