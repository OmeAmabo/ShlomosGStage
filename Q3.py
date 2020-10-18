def getSteps(W, N, x):
    counter = 0
    for i in range(W):
        counter += min(abs(W[i]-x), N-abs(W[i]-x))
    return counter


def getInput():
    W_len, N = [int(i) for i in input().split(' ')]
    W = [int(i) for i in input().split(' ')]

    return W_len, N, W



def testCase(case_num):
    



num_tests = int(input())
for i in range(num_tests):
    testCase(i + 1)
