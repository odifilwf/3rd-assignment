n = int(input())

c = 0
l = 0
h = 0
for i in range(1,n+1):
    n = int(input())
    if n == 0:
        c += 1
    elif n > 0:
        h += 1
    elif n < 0:
        l += 1
print(c,h,l)