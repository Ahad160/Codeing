class Programers:

    def Data(self,Name,Age,Post,P_Language):
        self.company="Microsoft"
        self.Name=Name
        self.Age=Age
        self.Post=Post
        self.P_Language=P_Language

    def Display(self):
        print(f"Company Name is {self.company}")
        print(f"Employe Name is {self.Name}")
        print(f"{self.Name} is {self.Age} Year Old")
        print(f"{self.Name} is in {self.Post} Post")
        print(f"{self.Name} Main Programing Language is {self.P_Language}")


object=Programers()


user=input("Enter Youer Name:")
user1=input("Enter Youer Age:")
user2=input("Enter Youer Post In The Company:")
user3=input("Enter Main Programing Language:")


object.Data(user, user1, user2, user3)

object.Display()