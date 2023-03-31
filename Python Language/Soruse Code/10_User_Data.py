class User:
    def data(self):
        print(f"User Name is {self.Name}\n")
        print(f"User Age is {self.Age} Year Old\n")
        print(f"User is in {self.Semester} Semester\n")

object = User()

object.Name="Raiden"
object.Age="19"
object.Semester='3rd'

object.data()