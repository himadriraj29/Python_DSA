def  palindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        modd = temp % 10
        rev = (rev * 10) + modd
        temp = temp // 10

    return (rev == n)

n = 56565
ans = palindrome(n)
print(ans)



