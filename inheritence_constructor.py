class Person :
    def __init__(self,name) :
        self.name = name
class Student(Person) :
    def __init__(self,name,roll) :
        super().__init__(name)
        self.roll = roll
s1 = Student("Mohan",32)
print(s1.name,s1.roll)