# Inheritance
# class GrandFather:  # Base/Parent Class
#     def grand_father(self):
#         print('I am grand father, I am base class')


class Father:  # Base/Parent Class
    def father_feature(self):
        print('This is father properties')


class Mother:  # Base/Parent Class
    def mother_feature(self):
        print('This is father properties')


class Son(Father):  # Derived/Child Class
    def son_feature(self):
        print('This is son properties')


class Daughter(Father, Mother):
    def daughter_feature(self):
        print('This is daughter properties')


s = Son()
d = Daughter()

s.son_feature()
s.father_feature()

d.daughter_feature()
d.father_feature()
# d.son_feature()
# f.father_feature()



