def solve(n,i,a,max):
  if (i == len(n)):
    output(a)
    return 
  elif (max < n[i] ):
    max = n[i]
    a = 1
  elif (max == n[i]):
    a +=1
  solve(n,i+1,a,max)
    
def output(a):
    print(str(n) + ': ' + str(a))

testcase = (int) (input())
for i in range(0, testcase):
    n = input()
    solve(n,0,1,'0')
    
  