#1
#
# for i in range(1,101):
#     print(i)
#



# #2
# for i in range(100,0,-1):
#     print(i)



# # #3
# for i in range(1, 101, 2):
#     print(i)



# #4
# for i in range(2,101,2):
#     print(i)



#5
# for i in range(0,101,5):
#     print(i)
#
#


#     #6
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i)



#7



# a = int(input())
# b = int(input())
#
# for i in range(a,b+1):
#     print(i)
# for i in range(a+1,b):
#     print(i)

# #8
# s = 0
# for i in range(1,101):
#     s += i
# print(s)




# #9
s = 0
# n = int(input())
# for i in range(1,n+1):
#     s += i
# print(s)



# #10
# for i in range(1,6):
#     a = int(input())
#     s += a
# print(s)



#while
# 1
n = 1
# while n != 0:
#     n = int(input())
#     s += n
# print(s)

#2
# pos = 0
# neg = 0
# while n != 0:
#     n = int(input())
#     if n > 0:
#         pos += 1
#     elif n < 0:
#         neg += 1
# print(f"pos")
# print(neg)


n = int(input())

n_s = n
s = 0

d = 1
dev = 10
while n // dev != 0:
    dev *= 10
    d += 1
print(f"{d} digits")

while d!=0:
    s += n_s // 10**d
    n_s %= 10**d
    d-=1
s += n % 10
print(f"sum {s}")


# Game

# import random as r
#
# n = r.randint(1,100)
#
# g = int(input())
#
# while g != n:
#     if  g > n:
#         print ("Too high")
#     else:
#         print ("Too low")
#     g = int(input())
# print("You win")
