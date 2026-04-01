class Student :
    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks
    def average(self) :
        sum = 0
        for i in self.marks :
            sum = sum + i
        print("hi, ",self.name,"Your Average is :",sum/3)
s1 = Student("Mohan",[90,92,93])
s2 = Student("Mehek",[99,98,99])
s3 = Student("Urvi",[95,96,97])
s1.average()
s2.average()
s3.average()