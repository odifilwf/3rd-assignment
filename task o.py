N = int(input())
ind = 0

for i in range(1,N+1):
    n = int(input())
    if n == 0:
        print("YES")
        ind=1
        break
if ind != 1:
    print("NO")
