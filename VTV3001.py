n = input()
n = int(n)

def solve(a,gt):
    gt *= a
    output(a, gt)
    if (n > a):
        return solve(a + 1,gt)

def output(testcase, output):
    print(str(testcase) + '! = ' + str(output))

print('0! = 1')
if (n == 0):
    exit()
solve(1,1)
