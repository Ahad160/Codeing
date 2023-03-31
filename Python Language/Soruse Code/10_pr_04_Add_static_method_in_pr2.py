class Calculator:
    def Square(self,num):
        square=num*num
        print(f"The Square of {num} is {square}\n")


    def Cube(self,num):
        cube=num*num*num
        print(f"The Cube of {num} is {cube}\n")
        

    def Square_Root(self,num):
        root=num**0.5
        print(f"The Square_Root of {num} is {root}\n")

    @staticmethod
    def Greetings():
        print("Wellcome Master Raiden\n")
    

object=Calculator()

user=int(input("Enter Number\n"))

object.Square(user)
object.Cube(user)
object.Square_Root(user)
object.Greetings()


