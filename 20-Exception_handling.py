# Irregularity


# a = 10
# b = 20
# # b = 'Mukund'
# try:
#     c = a + b
# except:
#     b = 0
#     c = a + b
#     print('This is exception code', c)
# else:
#     print('This is c from try :', c)
# finally:
#     print(c % 4)


# a = 15
# ZeroDivisionError
# print(a / 0)

# Value Error
# ModuleNotFoundError
# TypeError

# try:
#     a = int(input('Enter Positive number: '))
#
#     if a < 0:
#         raise ValueError('This is not a positive Number')
#     elif a == 1:
#         raise ZeroDivisionError('Zerorooo')
# except ValueError as v:
#     print(v)
# except ZeroDivisionError as z:
#     print(z)
# # except NameError as n:
# #     print(n)
# finally:
#     print('code is running')


# Python program to illustrate Function Annotations
def fib(n: 'int', output: 'list' = []) -> 'list':
    if n == 0:
        return output
    else:
        if len(output) < 2:
            output.append(1)
            fib(n - 1, output)
        else:
            last = output[-1]
            second_last = output[-2]
            output.append(last + second_last)
            fib(n - 1, output)
        return output

print(fib.__annotations__)

# print(fib(0, [15, 6, 25]))
