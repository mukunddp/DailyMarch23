# Polymorphism

# Many Form :
# + : Adding two number & Concatenation
# len()

# print(len('Mukund'))
# print(len(range(1, 15)))

# class ClassName:
#     def __init__(self, ):
#         print('This is constructor!')
#
#     def add(self, a, b, c):
#         return a + b + c
#
#     def add(self, a, b):
#         return a + b
#

# Method Overloading : Cannot be possible because bottom up approach
# single Class

# obj1 = ClassName()
# print(obj1.add(10, 15))


# print(obj1.add(15, 25, 36))


# Method Overriding : Run Time polymorphism
# Inheritance
# Same name of method & same parameters


class ClassName:
    def add(self, a, b, c):  # hidden
        return a + b + c


class ClassName2(ClassName):
    def add(self, a, b, c):  # invoked
        return a + b


c2 = ClassName2()
print(c2.add(15, 18, 16))
