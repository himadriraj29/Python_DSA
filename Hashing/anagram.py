def anagram(A):
    dis = {}
    n = len(A)
    for i in range(n):
        res = 0
        for j in A[i]:
            res += (ord(j) * ord(j))     
        if res not in dis:
            dis[res] = [i+1]
        else:
            dis[res].append(i+1)
    ans =[]
    for i in dis:
        ans.append(dis[i])
    return ans
if __name__ == '__main__':
    A = ['cat','dog','god','tac']
    ansr = anagram(A)
    print(ansr)


