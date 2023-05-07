from abc import ABC, abstractmethod  # ABC : Abstract Base Class


class Bank(ABC):  # Abstract Base Class
    @abstractmethod
    def manager(self):
        pass

    @abstractmethod
    def cashier(self):
        pass

    @abstractmethod
    def clark(self):
        pass


class BankBranch(Bank):     # abstract class
    @abstractmethod
    def sub_cashier(self):
        pass

    def sub_clark(self):
        print('Working on It!')


# b2 = BankBranch()
# b = Bank()
# b.manager()

class BankConcreate(BankBranch):
    def manager(self):
        print('I am gonna give you loan')

    def cashier(self):
        print("I have money")

    def clark(self):
        print('Come after Lunch ')

    def sub_cashier(self):
        print('caSH IS HERE!')


obj = BankConcreate()
obj.manager()
obj.clark()
obj.cashier()

