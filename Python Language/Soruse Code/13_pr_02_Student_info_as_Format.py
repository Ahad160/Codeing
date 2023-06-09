class Student:
    def __init__(self,name,mark,phone):
        self.name=name
        self.mark=mark
        self.phone=phone
        print("The Name of Student is {},his marks are {} and phone number is {}".format(name,mark,phone))

user=input("Enter Youer Name-")
user2=input("Enter Youer Marks-")
user3=input("Enter Youer Phoen_Number-")



object=Student(user,user2,user3)

