def Nbonaci(n,l):
    a = [0 for i in range(l)]
    a[n-1] = 1
    a[n] = 1

    for i in range(n+1,l):
        a[i] = 2 * a[i-1] - a[i - 1 - n]
    return a

n = 4
l = 8
ans = Nbonaci(n,l)
print(ans)

