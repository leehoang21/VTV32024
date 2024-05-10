def bin(n):
    if n < 1: 
        return ''
    return bin(n//2) + str(n%2)
    
def output(n):
    print(n)

testcase = (int) (input())
for i in range(0, testcase):
    a = (int) (input())
    n = bin(a)
    output(n)
    
    
  