class Parent :
    def money(self) :
        print("parent money")
class Child(Parent) :
    def bike(self) :
        print("child bike")
c1 = Child()
c1.bike()
c1.money()