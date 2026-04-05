class Person :
    def __init__(self,name) :
        self.name = name
class Student(Person) :
    def __init__(self,name,roll) :
        super().__init__(name)
        self.roll = roll
    def show(self) :
        print(self.name,self.roll)
c1 = Student("Mohan",54)
c1.show()