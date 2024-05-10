def solve(i):
    if i < 0:
        return 0
    if arr[i][0] == '-': 
        return solve(i-1)
    else:
      return 1 + solve(i-1)
    
def output(n):
    print(n)

testcase = (int)(input())
arr = input().strip().split(' ')
n = solve(testcase-1)
output(n)