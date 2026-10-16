x = int(input())

r = 0
while x > 0:
    r = r * 10 + x % 10
    x //= 10

print(r)