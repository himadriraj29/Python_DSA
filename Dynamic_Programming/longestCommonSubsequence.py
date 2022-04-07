def lcs(s1,s2,i,j):
    if i == 0 or j == 0:
        return 0
    elif s1[i] == s2[j]:
        return 1 + lcs(s1,s2,i-1,j-1)
    else:
        return max(lcs(s1,s2,i,j-1), lcs(s1,s2,i-1,j))

s1 = 'himadriraj'
s2 = 'mitaliraj'
print(lcs(s1,s2,9,8))