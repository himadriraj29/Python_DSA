def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
a = 12
b = 15
ans = gcd(12,15)
print(ans)