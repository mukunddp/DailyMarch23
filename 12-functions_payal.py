# l = [1,2,3,4]
#
# print([i//2 for i in l])


# for i in range(1,11):
#     print(i)

# for i in range(1,11):
#    pass
#    print("hi")


# for i  in range (1,11):
#     if i % 2 ==0:
#        # continue
#        break
#     print(i)

# for i in range (1, 12):
#     print(i)
#     continue
# else:
#     print("hi")


# num = 17
# # 17 * 1= 17
# for i in range(1,11): #n-1
#     print(f"{num} * {i} = {num*i}")


# a = "I am student"
#
# vowels = "aeiouAEIOU"
#
# for letter in a:
#     if letter in vowels:
#         print(letter)

# even = []
# odd = []
#
# for i in range(1,101):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even numer",even)
# print("odd numer",odd)


# while True:
#     year = int(input("enter thr year"))
#
#     if (year % 4 ==0) or (year % 400 ==0) and (year % 100 ==0):
#         print(year,"leap year")
#     else:
#         print(year,"is not leap year")


# Print all prime numbers in range


# low = 2
# high = 100
#
# for num in range(low,high+1): # start end value
#     for i in range(2,num):
#         if num % i ==0:
#             continue
#     else:
#         print(num)


# function


# def abc():#define the function
#     print("inside the function")
#
#
# abc() # calling the functions


# def add(a,b): #Positional Arguments
#     print("value of a", a, "\n value of b", b)
#
#
# add(34,12)


# def add(a ,b): #Keyword Arguments
#     print("value of a", a, "\n value of b", b)
#
#
# add(b =34,a =12)


# def add(a ,b,c): #mixed Arguments
#     print("value of a", a, "\n value of b", b, "\n value of c", c)
#
#
# add(10,b= 34,c=12)
#

# a = input("enter the string:")
#
#
# def response():
#     return a.upper()
#
#
# # a = input("enter the string:")
# print(response())


# def sub(a,b):
#     return  a-b
#
#
# print(sub(28,3))
# # print(add(12,34))


# def mul(a,b):
#     pass
#
# def sum(a,b):
#     print (a +b)
#
# sum(10,24)

# import module
# from module import *
#
# print(add(12,35))
#
#
# import time
# time.time_ns()

# def factorial(num):
#     if num == 1:
#         return 1
#     prev = 1
#     for i in range(2, num + 1):
#         prev *= i
#     return prev

# print(factorial(5))
# 4! = 4*3*2*1


# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num -1)
#
# print(factorial(5))
#
# [1]
# def sum(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#
#     else:
#         return num_list[0] + sum(num_list[1:])
#
#
# a
