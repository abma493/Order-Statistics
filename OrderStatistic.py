def RandSelect(A, l, r, i):
    if(l==r):
        return(A[l])
        
    z = RandPartition(A, l, r)
    k = z-l

    if(i==k):
        return(A[z])

def RandPartition(A, l, r):
    return
