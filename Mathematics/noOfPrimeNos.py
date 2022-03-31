def prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def noOfPrime(n):
    arr = []
    for i in range(1,n):
        if prime(i):
            arr.append(i)
    return arr

n = 10
ans = noOfPrime(n)
print(ans)