# 1
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5

# need to print 5 lines
# number in next line is increasing by 1 of last line
# number is starting from 1 and ends at 5
# for i in range(2, 7):  # 2, 3, 4, 5, 6
#     for j in range(1, i):
#         print(j, end=' ')
#     print()
#
# print('___________________ Next ______________________')
# 1  2  3  4  5
# 1  2  3  4
# 1  2  3
# 1  2
# 1

# need to print 5 lines
# number in next line is decrease by 1 of last line
# number is starting from 1 and ends at 5

# for i in range(0, 5):  # 0, 1, 2, 3, 4
#     for j in range(1, 6-i):
#         print(j, end=' ')
#     print()
#
# print('___________________ Next ______________________')

#            1
#          1   2
#        1   2   3
#      1   2   3   4
#    1   2   3   4   5


# need to print 5 lines
# space in next line is decrease by 1 of last line
# number in next line is increasing by 1 of last line
# number is starting from 1 and ends at 5

# for i in range(1, 6):  # 1, 2, 3, 4, 5
#     for j in range(1, 6-i):
#         print(end=' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

#           *
#         *  *
#       *  *  *
#     *  *  *  *
#   *  *  *  *  *

# for i in range(1, 6):  # 1, 2, 3, 4, 5
#     for j in range(1, 6-i):
#         print(end=' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

#             1
#          1  2
#       1  2  3
#    1  2  3  4
# 1  2  3  4  5

# for i in range(1, 6):  # 1, 2, 3, 4, 5
#     for j in range(1, 6 - i):
#         print(' ', end='  ')
#     for j in range(1, i + 1):
#         print(j, end='  ')
#     print()


# Armstrong Number
# 1^3 + 5^3 + 3^3 = 153

num = int(input('Please enter a number :'))
n_num = num
number_power = 0
while n_num / 10 != 0.0:
    n_num / 10
    a = n_num % 10
    n_num = n_num // 10
    number_power += a ** 3

if number_power == num:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not a armstrong number')
