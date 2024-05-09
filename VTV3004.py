def UCLN(a,b):
    if (b == 0):
        return a
    return UCLN(b, a % b)

def output(n):
    print(n)

testcase = (int) (input())
for i in range(0, testcase):
    a = input()
    b = input()
    n = UCLN(a,b)
    output(n)
    
  