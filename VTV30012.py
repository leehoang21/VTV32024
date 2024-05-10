def solve(i,n,arr):
  if (i >= n) :
    return 'Yes'
  elif (((float)(arr[i])) < 0):
    return solve(i + 1,n,arr)
  else: 
    return 'No'
  


def output(n):
    print(n)

testcase = (int) (input())
for i in range(0, testcase):
    n = (int) (input())
    arr = input().strip().split(' ')
    result = solve(0,n,arr)
    output(result)
    