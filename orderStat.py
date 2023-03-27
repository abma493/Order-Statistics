from random import randrange

def randSelect(A: list, l: int, r: int, i: int):
    if l == r:
        return A[l]
    z = randPartition(A, l, r)
    k = z - l

    if i == k:
         return A[z]
    elif i < k:
        return randSelect(A, l, z-1, i)
    else:
        return randSelect(A, z+1, r, i - k)



def randPartition(A, l, r):
    pivot = randrange(r)

    while l < r:

        while(A[l] <= pivot and l < r):
            l+=1
        while(A[r] >= pivot and l < r):
            r-=1
        swap(A, l, r)
    
    swap(A[pivot], A[l])


def swap(A, i1, i2):
    temp = A[i1]
    A[i1] = A[i2]
    A[i2] = temp

