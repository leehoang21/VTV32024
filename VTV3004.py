def UCLN(a,b):
    if (b == 0):
        return a
    return UCLN(b, a % b)

def output(n):
    print(n)

testcase = (int) (input())
for i in range(0, testcase):
    x = input().split(' ')
    a = (int)(x[0])
    b = (int)(x[1])
    if(a > b):
        n = UCLN(a,b)
    else:
        n = UCLN(b,a)
    output(n)
    
  