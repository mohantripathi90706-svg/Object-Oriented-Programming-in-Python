class Parent :
    def __init__(self) :
        print("Parent is Coming")
class Child(Parent) :
    def __init__(self) :
        super().__init__()
        print("Parent is Gone")
c1 = Child()