# Encapsulation

# setting the Restriction
# Access Specifiers

# public
# protected
# private

class MyClass:
    def __init__(self):
        self.name = 'Mukunda'
        self._debit_card = 646651646466515541  # Protected
        self.__pin = 4564654  # private

    def method(self):
        return self.name, self._debit_card, self.__pin


class MyClass2(MyClass):
    def method2(self):
        return self.name, self._debit_card, self.__pin


# obj = MyClass()
# # print(obj.name)
# # print(obj._debit_card)
# # print(obj.__pin)
#
# print(obj.method())
# obj2 = MyClass2()
# obj2.method2()


# class test:
#     def __init__(self, a="Hello World"):
#         self.a = a
#
#     def display(self):
#         print(self.a)
#
#
# obj = test()
# # obj.init()
# obj.display()

class fruits:

    def __init__(self, price):
        self.price = price


obj = fruits(50)

obj.quantity = 10

obj.bags = 2

print(obj.quantity + len(obj.__dict__))
# print(obj.__dict__)