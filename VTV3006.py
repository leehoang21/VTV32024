from math import sqrt


def solve(n):
    if n < 1: 
        return 0
    return sqrt(n + solve(n-1))
    
def output(n):
    result = "{:.10f}".format(n)
    print(result)

testcase = (int) (input())
for i in range(0, testcase):
    a = (int) (input())
    n = solve(a)
    output(n)
    
    
  