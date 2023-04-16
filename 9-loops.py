persons = [{
    'name': 'Mukund',
    'age': 25
},
    {
        'name': 'Gaurav',
        'age': 26
    },
    {
        'name': 'Aarti',
        'age': 24
    },
    {
        'name': 'Akshay',
        'age': 20
    },
    {
        'name': 'Tejas',
        'age': 23
    }]

# in - (Membership operator)
# list_person_above_23 = []
#
# for variable in 'Mukund':        # iterables
#     if variable ==  'M':
#         list_person_above_23.append(variable)
#
# print('All Persons :', persons, '\n')
# print('Person above age 23', list_person_above_23)


# for i in range(0, 15):      # 0, 15-1 = 14
#     print('Mukund')         # 14(1) or 15(2) or 0(1)


# print table of 17 or 23 or 27 :
# for i in range(1, 11):
#     print(17 * i)   #
# 12 * 1 = 12
# 12 * 2 = 24
# 12 * 3 = 36
# 12 * 4 = 48
# 12 * 5 = 60# 12 * 2 = 2
# n = 5
# while n == 6:
#     number = int(input('Enter the number to get table :'))
#     for i in range(1, 11):  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#         print(i * number, end=', ')
#     print(f'\nThis is your table of {number}')
import time

# num = 2
# i = 0   # 0
# while True:
#     i = i + 1  # 1, 2, 3, 4, 5, 6
#     print(num*i)

# a = 100
# b = 500
# for i in range(a, b+1):  # 100 -> 500
#     if (i % 2) != 0:
#         print(i)


# Security bot using while loop

# Create list of Users
# Ask user to enter his name
# If name is present in System allow to enter.  # You are allowed inside
# Else ask admin to add his name into system    # ADMIN
# If admin says Yes then
#       - ask users details
#       - user will get added inside the users list

users = [{'name': 'Mukund Parve', 'age': 25, 'clg': 'PCCOE, Pune'},
         {'name': 'Gaurav', 'age': 26, 'clg': 'Tech Amplifiers, Pune'},
         {'name': 'Aarti', 'age': 25, 'clg': 'Tech Amplifiers, Pune'},
         {'name': 'Akshay', 'age': 26, 'clg': 'Tech Amplifiers, Pune'},]
