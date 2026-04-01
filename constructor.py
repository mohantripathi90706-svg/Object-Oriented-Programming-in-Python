class Student :
    def __init__(self,name,marks) :
        self.name = name
        self.__marks = marks
    def display(self) :
        print(self.name,self.__marks)
s1 = Student("mohan",32)
s1.__marks = 50
print(s1.__marks)
s1.display()
print(vars(s1))