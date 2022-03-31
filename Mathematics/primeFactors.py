def prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primeFactors(n):
    arr = []
    for i in range(1,n):
        if prime(i): 
            x = i
            while n % x == 0:
                arr.append(x)
                x = x * i
    return arr

n = 15
ans = primeFactors(n)
print(ans)


