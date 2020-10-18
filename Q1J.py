START_FRAG = "KICK"
END_FRAG = "START"

def getNumberOfTests():
    return int(input())

def getNextTest():
    return input()

def printSingleTest(testNumber, counter):
    print("Case #" + str(testNumber+1) + ": " + str(counter))

def runSingleTest(testNumber, test):
    tempCounter = 0
    finalCounter = 0
    for i in range(len(test)-4):
        if END_FRAG == test[i:len(END_FRAG)+i]:
            finalCounter += tempCounter
        if START_FRAG == test[i:len(START_FRAG)+i]:
            tempCounter += 1
    printSingleTest(testNumber, finalCounter)

def runTests():
    numOfTests = getNumberOfTests()
    for i in range(numOfTests):
        test = getNextTest()
        runSingleTest(i, test)

runTests()

