a = [2, 5, 8, 11, 14, 17, 20]

sum = 0

APlength = len(a)

for i in range(0, APlength):
  if a[i] == a[APlength-1]:
    print("nth term is: ",a[1])

for i in range(0, APlength):
  sum = sum + a[1]

print("Sum of Arithemetic series is: ", sum)