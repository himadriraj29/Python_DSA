def digit(n):
    count = 0
    while n != 0:
        n = n//10
        count += 1
    return count
n = 56784
ans = digit(n)
print(ans)