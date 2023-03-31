class Calling:
    def __init__(self,name,semester,p_language):
        self.name=name
        self.semester=semester
        self.p_language=p_language

    def Display(self):
        print(f"\n\nThe Name is {self.name}")
        print(f"{self.name} is in {self.semester}rd")
        print(f"{self.name} is learing {self.p_language}")



user1=input("Enter Youer Name\n")
user2=input("Enter Youer semester\n")
user3=input("Enter the Name of programing language that you are learning\n")


object=Calling(user1,user2,user3)

object.Display()
