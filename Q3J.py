
def getSteps(W, N, x):
    counter = 0
    #implement
    return counter

def binarySearchWithBranch(W, N, low, high, branchInLeft):
    mid = (low + high) / 2

    while low < high:
        x = getSteps(W, N, mid)

        if mid == 0:
            x_u = getSteps(W, N, 1)
            if x_u < x:
                return 1
            else:
                return 0
        if mid == N-1:
            x_l = getSteps(W, N, N - 2)
            if x_l < x:
                return N-2
            else:
                return N-1

        x_l = getSteps(W, N, mid-1)
        x_u = getSteps(W, N, mid+1)

        if x_l >= x and x_u >= x:
            return mid

        if x_l < x:
            high = mid
        elif x_u < x:
            low = mid

        mid = (low + high) / 2

def cyclicBinarySearch(W, N):
    low = 2
    high = N
    mid = (low+high)/2
    startAt = mid

    while low < high:
        x = getSteps(W, N, mid)

        if mid == 2:
            if x > getSteps(W, N, N):
                return binarySearchWithBranch(W, N, startAt, N, True)
            else:
                return mid
        if mid == N:
            if x > getSteps(W, N, 2):
                return binarySearchWithBranch(W, N, 2 ,startAt, False)
            else:
                return mid

        x_l = getSteps(W, N, mid-1)
        x_u = getSteps(W, N, mid+1)

        if x_l >= x and x_u >= x:
            return mid

        if x_l < x:
            high = mid
        elif x_u < x:
            low = mid

        mid = (low + high) / 2

    return mid