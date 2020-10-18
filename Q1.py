def testCase(case_num):
    input_string = input()

    strKick, strStart = 'KICK', 'START'
    kickCount, validCount = 0,0

    current = 0
    while current + len(strStart) - 1 < len(input_string):
        if input_string[current:current + len(strKick)] == strKick:
            kickCount += 1
        elif (input_string[current:current + len(strStart)] == strStart):
            validCount += kickCount
        current += 1
    print('Case #' + str(case_num)+ ': ' + str(validCount))



num_tests = int(input())
for i in range(num_tests):
    testCase(i+1)