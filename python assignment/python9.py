
t = int(input())
for i in range(t):
 n = int(input())
 maxleft = -1
 result = 0
 for a in range(1,n+1):
  left = n % a
  if left > maxleft:
    result = a
 print(result)