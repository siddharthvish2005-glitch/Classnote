n = int(input())

for i in range(n):
  a,b = input().split()
  a=int(a)
  b=int(b)

  ans = 1
  for j in range(b):
    ans = (ans * a) % 10

  print(ans)  