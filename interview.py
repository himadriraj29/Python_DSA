# function to take input
def get_in(r,c):
    M = []
    for i in range(r):
        M.append([])
        for j in range(c):
            M[i].append(input())
    return M
# now we will look for sequence
def getSeq(M,r,c):
    B = 0
    k = -1
    seq = []
    ## Each time we enter a row we add array for B's in that line
    for i in range(r):
        seq.append([])
        k += 1
        for j in range(c):
            ## if we encounter B we increase it's count 
            if M[i][j] == 'B':
                B += 1
            # noe if w comes we will add B to ans and set B to 0
            elif M[i][j] == 'W' and B != 0:
                seq[k].append(B)
                B = 0
        # at last when we are done in this row
        if B != 0:
            seq[k].append(B)
            B = 0
    return seq

if __name__ == "__main__":
    M = [['W','W','W','W'],['B','W','W','W'],['B','W','B','B'],['W','W','B','W'],['B','B','W','W']]

    ans = getSeq(M,len(M),len(M[0]))
    print(ans)
