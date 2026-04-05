class Person :
    def __init__(self,name) :
        self.name = name
class Person1 :
    def __init__(self,roll) :
        self.roll = roll
class Person2 :
    def __init__(self,age) :
        self.age = age
class Person3(Person,Person1,Person2) :
    def __init__(self,name,roll,age) :
        Person.__init__(self,name)
        Person1.__init__(self,roll)
        Person2.__init__(self,age)
    def show(self) :
        print(self.name,self.roll,self.age)
c1 = Person3("Mohan",52,19)
c1.show()