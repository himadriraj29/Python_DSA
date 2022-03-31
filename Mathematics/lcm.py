def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
def lcm(a,b):
    return a*b//gcd(a,b)
a = 12
b = 15
ans = lcm(12,15)
print(ans)
