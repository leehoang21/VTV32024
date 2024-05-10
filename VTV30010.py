def gt(n):
    if (n < 2):
        return 1
    return n * gt(n-1)

def solve(n,x):
    if (n < 1):
        return 0
    return (x**n/gt(n)) + solve(n-1,x)

def output(n):
    result = "{:.8f}".format(n)
    print(result)

testcase = (int) (input())
for i in range(0, testcase):
    arr = input().strip().split(' ')
    x = (float) (arr[0])
    n = (int) (arr[2])
    a = solve(n,x)
    output(a)