def testCase(case_num):
    N = int(input())
    arr = [0]*(2*N-1)
    max = 0

    for i in range(N):
        newInput = list(input().split(' '))
        for j,coins in enumerate(newInput):
            arr[N-1-i+j] += int(coins)
            if(arr[N-1-i+j] > max):
                max = arr[N-1-i+j]

    print('Case #' + str(case_num) + ': ' + str(max))


num_tests = int(input())
for i in range(num_tests):
    testCase(i+1)