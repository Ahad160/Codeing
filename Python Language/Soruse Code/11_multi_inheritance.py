class Parents:
    Name="Raiden"

class Parents_2:
    Age=19


class Child(Parents,Parents_2):
    def display(self):
        print(f"Name is {self.Name}")
        print(f"Age is {self.Age}")

        
object=Child()


object.display()