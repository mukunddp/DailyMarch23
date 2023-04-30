# def fun(a, b, c, d, e):
#     return a + b + c + d + e
#
#
# # print(fun(10, 15, 12, 65, 23))
# # lambda arguments : expression
# x = lambda a, b, c, d, e: a + b + c + d + e
# print(x(10, 15, 12, 65, 23))
# print(print("Mukund"))


# x = lambda a, b: a * b
# print(x(5, 6))
# print(x(6, 6))
# print(x(8, 6))


# x = lambda a, b, c: a + b + c
# print(x(5, 15, 25))


# def func(n):
#     return lambda a: a * n


# double = func(2)  # lambda a: a * 2
# triple = func(3)  # lambda a: a * 3
# #
# for i in range(1, 11):
#     print(double(i))
# print(triple(11))


# write a lambda function to calculate sum of n numbers
# (n/2)*(2*a + (n-1)*d)
# a = 1
# d = 1
# n = 100

# sum = lambda n: (n / 2) * (n + 1)
# print(sum(100))

# MAP :
# map(function, iterables )

# print(sum(15))
# print(sum(17))

# def sum(n, m):
#     return (n / 2) * (m + 1)
#
#
# print(list(map(sum, [15, 17, 100], [15, 17, 100])))

# def add(a, b):
#   return a + b
#
# x = map(add, (10, 15, 25), (12, 14, 16))
# print(list(x))


# Write one line code to
# calculate squares of given numbers in list
# nums = [15, 17, 23, 27, 29, 53, 27, 19, 64]

print(list(map(lambda n: n * n, [15, 17, 23, 27, 29, 53, 27, 19, 64])))
# print(list(map(lambda n: n * n, [15, 17, 23, 27, 29, 53, 27, 19, 64])))
