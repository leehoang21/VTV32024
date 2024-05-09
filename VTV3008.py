from math import sqrt

def solve(i):
    if i < 0:
        return 0
    if ((float)(arr[i])) % 2 == 0: 
        return (float)(arr[i]) + solve(i-1)
    else:
        return solve(i-1)
    
def output(n):
    print(n)

testcase = (int)(input())
a = input().split(' ')
arr = []
for i in range(0,testcase):        
    arr.append((float(a[i])))
n = solve(testcase-1)
output(n)