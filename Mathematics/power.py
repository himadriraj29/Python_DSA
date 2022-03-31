def power(a,b):
    res = 1
    for i in range(b):
        res = a * res
    return res

a = 3
b = 4
ans = power(3,4)
print(ans)