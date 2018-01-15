############################################# recursion

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
#
#
# print (fact(4))
#
############################################# timedelta
#
# from datetime import date
#
# a = date(2018,1,3)
# b = date(1991,11,18)
#
#
# print((a-b).days/365)

############################################# square_sum


# def square_sum(n):
#     if n==1:
#         return 1
#     else:
#         return n**2 + square_sum(n-1)

#
# print(square_sum(4))

########################################## keywords

# import keyword
#
# print(keyword.kwlist)
# print(len(keyword.kwlist))

###################################### pythagoras theorem
# a**2 + b**2 = c**2
######################################reverse list
#### [::-1] to reverse list

####################################### subprocess
# import subprocess
#
# c = subprocess.call(["ls"])
###################################### set
#
# s = [1,5,7,3,5,7,8,3,2,7]
# a = set(s)
# print(a)

###################################### subset and super set

# s1 = {1,2,3}
# s2= {2,3}
#
# print(s1 > s2) # or s1.issuperset(s2)
# print(s1 < s2)# or s1.issubset(s2)
# s3 = s1.union(s2)
# s4 = s1.intersection(s2)
# s5 = s1 - s2 or s1.difference(s2)

###################################### enumerate
#
# s = [1,3,5,7,9]
#
# for i,j in enumerate(s): # displays the index of the value as well
#     print(i,j, end=",")

###################################### list comprehension
#
# use [] for list
# use {} for set


# a  = [x for x in range(1,20)]
# b  = [x for x in range(1,20) if x % 2 == 0] # to print even numbers from the range
# c  = [x**2 for x in range(1,20) if x % 2 == 0] # to print even numbers from the range and get square of the numbers
#
# print(c)

###################################### dict comprehension

# a= {x:x*x for x in range(1,10)} # to get square of all the numbers in range in dict

# print(a)


###################################### lambda function

# def f(x,y,z):
#     return x+y+z
# print(f(5))
# #### SIMILAR TO #########
# a = lambda y,x,z : y+x+z
#
# print(a(3,4,5))

###################################### map function
#
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def sqr(x):
#     return x * x
#
#
# a = ([sqr(x) for x in s]) # list comprehension
# b = (list(map(sqr,s))) # or it can be don by using map function
#
# print(a,b)

###################################### reduce or reduction fucntion

# from functools import reduce
#
# a= reduce(lambda x,y : x*y ,[1,2,3,4,5,6,7,8])
#
# print(a)
#
########################################## global keyword
#

# we can not write the same variable in defined outside the to inside we need to use the global keyword
# we can read without changing the global varible in any class or fucntion but cant write.


# a=10
#
# def p():
#     print(a)
#
#
# def increment():
#     global a # this will change the variable defined outside the any class or any function
#              # if we dont use global here then the value of a will be 11 but inside the fucntion and the variable
#              # which is outside the fucntion will not be change
#     a = 11
#     print(a)
#
#
# p()
# increment()

####################################### diff between non local or global
# x = 10 # global x


# def s():
#     x = 10
#
#     def g():
#         # nonlocal x
#         x = 15
#         return x * x
#     print(g())
#
#
# s()