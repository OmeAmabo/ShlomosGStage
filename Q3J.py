
def getSteps(W, N, x):
    counter = 0
    for i in range(W):
        counter += min(abs(W[i]-x), N-abs(W[i]-x))
    return counter

def binarySearchWithBranch(W, N, low, high, branchInLeft, startValue):
    #private
    mid = (low + high) / 2
    x = getSteps(W, N, mid)

    while low < high:
        if mid == 0:
            x_u = getSteps(W, N, 1)
            if x_u < x:
                return x_u
            else:
                return x
        if mid == N:
            x_l = getSteps(W, N, N - 1)
            if x_l < x:
                return x_l
            else:
                return x

        x_l = getSteps(W, N, mid-1)
        x_u = getSteps(W, N, mid+1)

        if x_l >= x and x_u >= x:
            return x

        if x_l < x:
            if branchInLeft and startValue < x:
                low = mid
            else:
                high = mid
        elif x_u < x:
            if not branchInLeft and startValue < x:
                high = mid
            else:
                low = mid

        mid = (low + high) / 2
        x = getSteps(W, N, mid)

    return x

def cyclicBinarySearch(W, N):
    low = 2
    high = N
    mid = (low+high)/2
    startAt = mid
    startValue = getSteps(W, N, startAt)
    x = getSteps(W, N, mid)

    while low < high:
        if mid == 2:
            if x > getSteps(W, N, N):
                return binarySearchWithBranch(W, N, startAt, N, True, startValue)
            else:
                return x
        if mid == N:
            if x > getSteps(W, N, 2):
                return binarySearchWithBranch(W, N, 2 ,startAt, False, startValue)
            else:
                return x

        x_l = getSteps(W, N, mid-1)
        x_u = getSteps(W, N, mid+1)

        if x_l >= x and x_u >= x:
            return x

        if x_l < x:
            high = mid
        elif x_u < x:
            low = mid

        mid = (low + high) / 2
        x = getSteps(W, N, mid)

    return x