import random

random=random.randint(1, 40)

class Auto:
    def __init__(self,R_Num):
         i=10
         time=0
         while i == 10:
            user=int(input("Enter a number\n"))
            if user<R_Num:
              print("Guess A Big Number")
              time=time+1
            elif user>R_Num:
              print("Guess A Small Number")
              time=time+1
            elif user==R_Num:
              print(f"You Guess The right Number At {time} Times\n")              
              break

object=Auto(random)