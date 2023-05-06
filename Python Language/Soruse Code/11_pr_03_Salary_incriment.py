class Employe:
    Salary=5000
    incriment=1.5


    @property
    def After_Salary_incriment(self):
        return f"Salary is {self.Salary*self.incriment}"    

    @After_Salary_incriment.setter
    def After_Salary_incriment(self,amount):
        self.incriment=amount/self.Salary


object=Employe()

print(object.After_Salary_incriment)

print(object.incriment)

object.After_Salary_incriment=2000

print(object.incriment)
