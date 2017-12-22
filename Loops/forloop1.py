# n = int(input(" number : "))
# n = 5
for i in range(0,6):
    for j in range(i,i+2):
        print("",end=" ")
    for s in range(5-i+2):
        print("*", end=" ")
    for x in range(5-i+1):
        print(" ", end=" ")
    print(" ")

#
# for i in range (1,7):
#     for j in range (1,i):
#         print(j, end=" ")
#     print("")

# for i in range (1,7):
#     for j in range (i,i+1):
#         for s in range(j):
#             print(end=" ")
#
#     print(" ")