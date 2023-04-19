# Security bot using while loop

# Create list of Users
# Ask user to enter his name
# If name is present in System allow to enter.  # You are allowed inside
# Else ask admin to add his name into system    # ADMIN
# If admin says Yes then
#       - ask users details
#       - user will get added inside the users list

# Create list of Users
users = [{'name': 'Mukund Parve', 'age': 25, 'clg': 'PCCOE, Pune'},
         {'name': 'Gaurav', 'age': 26, 'clg': 'Tech Amplifiers, Pune'},
         {'name': 'Aarti', 'age': 25, 'clg': 'Tech Amplifiers, Pune'},
         {'name': 'Akshay', 'age': 26, 'clg': 'Tech Amplifiers, Pune'}, ]

# If name is present in System allow to enter.  # You are allowed inside
name_users = set()
user_details = {'name': None, 'age': None, 'clg': None}

while True:
    for i in users:
        name_users.add(i['name'])
    print(name_users)
    # Ask user to enter his name
    user_input_name = input('Enter your name: ').title()
    if user_input_name in name_users:
        print(f'Hello {user_input_name}! Please come Inside!!')
    # Else ask admin to add his name into system    # ADMIN
    else:
        print('Sorry your are not added into user list !')
        # Do you want to add this person into system?
        admin_response = input('\nDo you want to add this person into system? Type- {Yes/No}').title()
        if admin_response == 'Yes':
            # Ask user to enter his details
            is_this_name = input(f'Is this your correct name {user_input_name} ? Type- {{Yes/No}}').title()
            if is_this_name == 'No':
                name = input('Enter your correct name: ')
                user_details['name'] = name
            else:
                name = user_input_name
                user_details['name'] = name
            age = int(input('Enter your age : '))
            user_details['age'] = age
            clg = input('Enter your college name: ')
            user_details['clg'] = clg
            # add that user into system
            users.append(user_details)
            print('Congratulations! You are added into System. ')
        else:
            print('Sorry You are not Allowed !')
