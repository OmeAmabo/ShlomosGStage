def getNumberOfTests():
    return int(input())

def getNextTest():
    return int(input())

def getNextRow():
    return input().split()

def printSingleTest(testNumber, counter):
    print("Case #" + str(testNumber+1) + ": " + str(counter))

def getMax(hist):
    max = hist[0]
    for i in range(len(hist)):
        if hist[i] > max:
            max = hist[i]
    return max

def runSingleTest(testNumber, N):
    numOfDiagonals = 2*N - 1
    hist = [0] * (numOfDiagonals)
    for row in range(N):
        NextRow = getNextRow()
        for col in range(N):
            hist[N-1+col-row] += int(NextRow[col])

    printSingleTest(testNumber, getMax(hist))

def runTests():
    numOfTests = getNumberOfTests()
    for i in range(numOfTests):
        rows = getNextTest()
        runSingleTest(i, rows)

runTests()