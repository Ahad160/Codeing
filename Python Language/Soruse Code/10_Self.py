class employe:
    company="Youtube"
    def getsalary(self,clcode):
        print(f"The company name is {self.company} And salary is {self.salary}\nclient code is {clcode}")

object=employe()

object.salary=5000

object.getsalary(568) # employe.getsalary(object) 