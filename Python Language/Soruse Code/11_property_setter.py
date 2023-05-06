class Parent:
    Goal="Doctor"
    Salary=5000000

    @property        #By Useing This You can call this as a property and not a Function
    def Function(self):
        Display=print(f"Parant Want to be his son a {self.Goal} And Wants Salary {self.Salary}")
        return Display


    @Function.setter
    def change(self,num):
        self.Salary=num

   
    def Display(self):
        self.Goal="Cyber_Assaassin"


object=Parent()

object.change=700

object.Display()


object.Function



# print(object.Salary)

# print(object.Display())

