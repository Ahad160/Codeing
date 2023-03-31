class Parents:
    def Task(self):
        print("Learn Quran Sorif ")

class Child_1(Parents):
     def Play1(self):
        print("Want To Play Mobile Legend")
        # Learn="Youtube Videos"

class Child_2(Child_1):
    def Play2(self):
        print("Want To Play Hitman 2016")
        super().Play1()
         # Learn="Python"




object=Child_2()


object.Play2()