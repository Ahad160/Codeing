class Parents:
    company="Google"
    def display(self):
        print(f"The Company is {self.company}")

class child(Parents):
    language="Python"
    def first(self):
        print(f"The language is {self.language}")
        print(f"The Company is {self.company}")

object=Parents()

object2=child()

object2.display()



