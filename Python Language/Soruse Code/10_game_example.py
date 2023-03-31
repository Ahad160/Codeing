class Control:
    def Press1(self):
        object2.Moveleft()
    def Press2(self):
        pass
    def Press3(self):
        pass
    def Press4(self):
        pass

class Diretion:
    def Moveleft(self):
        print("User is Moveleft\n")
    def MoveRight(self):
        print("User is Moveright\n")
    def MoveUp(self):
        print("User is Moveup\n")
    def MoveDown(self):
        print("User is Movedown\n")


object=Control()
object2=Diretion()

user=2

if user == 2:
    object.Press1()
