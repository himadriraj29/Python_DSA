def divisors(n):
    arr = []
    for i in range(1,n+1):
            if n % i == 0:
                arr.append(i)              
    return arr

n = 15
ans = divisors(n)
print(ans)