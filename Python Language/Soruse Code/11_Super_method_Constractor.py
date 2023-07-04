class Parents:
    
    def __init__(self):
        print("This is Parents Class")

    def Task(self):
        print("Learn Quran Sorif ")

class Child_1(Parents):

    def __init__(self):
        super().__init__()
        print("This is Child_1 Class")

    def Play1(self):
        print("Want To Play Mobile Legend")
        # Learn="Youtube Videos"

class Child_2(Child_1):
    def __init__(self):
        super().__init__()
        print("This is Child_2 Class")

    def Play2(self):
        print("Want To Play Hitman 2016")
        # super().Play1()
         # Learn="Python"




object=Child_1()


# object.Play2()