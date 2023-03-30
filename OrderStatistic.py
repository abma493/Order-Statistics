import random

#Order Statistic algorithm to obtain the n-th smallest element
def RandSelect(A, l, r, i):

    if(l==r):
        return(A[l])
        
    z = RandPartition(A, l, r)
    k = z - l # rank of the pivot in respect to the subarray

    if i == k:
        return(A[z])
    elif i < k:
        return RandSelect(A, l, z-1, i)
    else:
        return RandSelect(A, z+1, r, i-k-1)


def RandPartition(A, l, r):

    randPivot = random.randint(l, r)

    A[l], A[randPivot] = A[randPivot], A[l] #swap

    pivot = A[l] # pivot value
    i = l # left pointer in array
    for j in range(l+1, r+1): #Must be inclusive, hence r+1
        if A[j] <= pivot:
            i+=1
            A[j], A[i] = A[i], A[j] # swap
    
    A[l], A[i] = A[i], A[l] #swap

    return i