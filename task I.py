x = int(input())
c = 0
i = 1
while i * i <= x:
  if x % i == 0:
    if i * i == x:
      c += 1
    else:
      c += 2
  i += 1
print(c)