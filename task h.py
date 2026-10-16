x = int(input())

n = 1
while x != n-1:
    if x % n == 0:
        print(n, end=" ")
    n += 1