class Train:
    def __init__(self,Name,Fare,Seats):
        self.Name=Name
        self.Fare=Fare
        self.Seats=Seats

    def Status(self):
        print("🟡🟡🟡🟡🟡🟡🟡")
        print(f"Train Name is {self.Name}\n")
        print(f"Available Seats in this train is {self.Seats}\n")
        print("🟡🟡🟡🟡🟡🟡🟡")

    def Fare_info(self):
        print(f"The Train Fare is Rupes:{self.Fare}")


    def Book_Ticket(self):
        if self.Seats>0 :
            print("Youer Train Ticket is booked\n")
            self.Seats=self.Seats-1


object=Train("Andhra Pradesh Express 12724", 60, 400)


object.Status()
object.Fare_info()

object.Book_Ticket()

object.Status()



