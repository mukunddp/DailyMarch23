# classes

# class MyClass:
#     a = 10
#     b = 20

# obj = MyClass()
# obj.a = 52
# print(obj.a)
#
# obj2 = MyClass()
# obj2.a = 20
# print(obj2.a)
#
# print(obj.a)

#
# class MyClass:
#
#     def __init__(self):
#         print('I am Constructor')
#
#     def method_a(self):
#         self.a = 50
#         print("Method A")
#
#     def method_c(self):
#         print(self.a)
#         print('Method B')
#
#
# obj = MyClass()
# obj.method_a()


# class MyClass:  # Class
#
#     def __init__(self, a, b):  # Constructor
#         self.a = a
#         self.b = b
#         print('I am Constructor')
#
#     def method_a(self):  # Method
#         print(self.a)
#         print("Method A")
#
#
# obj = MyClass(10, 15)
# obj.method_a()

# Write a class with personal details like - name, clg, mob, email, etc
# constructor parameterized
# define methods in class and will ask for details separately
# personal details - name, age
# contact details - mob, email
# educations details - clg, eduction ,

class Details:
    def __init__(self, name, clg, mob, email, age, degree):  # Constructor - default / parameterized
        self.name = name
        self.clg = clg
        self.mob = mob
        self.email = email
        self.age = age
        self.degree = degree

    def personal_details(self):
        print(f"Personal Details : \nName : {self.name} \nAge: {self.age}")

    def contact_details(self):
        print(f"Contact Details: \nMobile : {self.mob} \nEmail : {self.email}")

    def education_details(self):
        print(f"Educational Details: \nCollege : {self.clg} \nDegree : {self.degree}")

    def contact_etails(self):
        print(f"Contact Details: \nMobile : {self.mob} \nEmail : {self.email}")


obj = Details('Mukund Parve', 'PCCOE, Pune', 7972005157, 'mukundparve@gmail.com0', 25, 'BE Mechanical')
obj.personal_details()
print()
obj.contact_details()
print()
obj.education_details()
