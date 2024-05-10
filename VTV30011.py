def Xn(n):
    if n == 0 :
        return 1
    return Xn(n-1) + Yn(n-1)

def Yn(n):
    if (n == 0):
        return 0
    return 3*Xn(n-1) + Yn(n-1)

def output(n):
    print(str(Xn(n)) + " " + str(Yn(n)))

testcase = (int) (input())
for i in range(0, testcase):
    n = (int) (input())
    output(n)