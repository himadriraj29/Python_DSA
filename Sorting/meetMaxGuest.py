def meetMaxGuest(arv, dep):
    arv.sort()
    dep.sort()
    maxi = float('-inf')
    guest = 0
    i = 0
    j = 0
    n = len(arv)
    while i < n:
        if arv[i] < dep[j]:
            guest += 1
            i += 1
        elif arv[i] > dep[j]:
            guest -= 1
            j += 1
        else:
            i += 1
            j += 1

        if guest > maxi:
            maxi = guest
    return maxi

arv = [900, 940,950, 1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]
ans = meetMaxGuest(arv, dep)
print(ans)
