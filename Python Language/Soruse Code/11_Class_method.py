class Parent:
    Name='Raiden'
    Ripermode=False

    # def change_ripermode(self,mode):        #It Just Add a intanse atruibute,But not gonna change class atribute
    #     Ripermode = mode
    #     print(f"Riper Mode is {Ripermode}")


    @classmethod
    def change_ripermode(cls,mode):             # gonna change class atribute
        cls.Ripermode = mode
        print(f"Riper Mode is {cls.Ripermode}")



object=Parent()

print(object.Ripermode)

object.change_ripermode(True)

print(object.Ripermode)

