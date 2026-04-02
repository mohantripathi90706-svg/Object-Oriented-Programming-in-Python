class Bank :
    def __init__(self) :
        print("This Bank is Safe")
class Sbi :
    def __init__(self) :
        print("yes , SBI is always a safe Bank")
class Icci(Sbi,Bank) :
    # def __init__(self) :
        # print("All Bank is safe")
    pass
c1 = Icci()