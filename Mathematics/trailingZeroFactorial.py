def countTrailingZero(n):
    res = 0
    i = 5
    while i <n:
        i = i * 5
        res = res + n//i
    return res
n = 251
ans = countTrailingZero(n)
print(ans)