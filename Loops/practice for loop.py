# n = 5
# for i in range (n):
#     for s in range(i,n):
#         print("",end=" ")
#     for x in range(n-i-i):
#         print(" * ",end=" ")
#     print(" ")

#
# for raw in range(7):
#     for col in range(4):
#         if
#             print(" *", end="")
#         else:
#             print(end=" ")
#     print(" ")
#

n=5
num = 0

for i in range (n):
    for x in range (i,n-1):
        print(" ", end="")
    for j in range (i+1):
        print(num,end=" ")
        num += 1
    print("")