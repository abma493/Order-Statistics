import random

#Order Statistic algorithm to obtain the n-th smallest element
def RandSelect(A, l, r, i):
    if(l==r):
        return(A[l])
        
    z = RandPartition(A, l, r)
    k = z-l

    if(i==k):
        return(A[z])
    elif(i<k):
        return RandSelect(A, l, z-1, i)
    else:
        return RandSelect(A, z+1, r, i-k-1)


def RandPartition(A, l, r):
    randPivot = random.randint(l, r)
    A[l], A[randPivot] = A[randPivot], A[l]

    x = A[l]
    i = l
    for j in range(l+1, r+1): #Must be inclusive, hence r+1
        if(A[j]<=x):
            i+=1
            A[j], A[i] = A[i], A[j]
    
    A[l], A[i] = A[i], A[l]
    return i