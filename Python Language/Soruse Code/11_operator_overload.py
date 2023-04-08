class Parent:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
       return (f"{self.i}i+{self.j}j+{self.k}k")

    def __add__(self,num):
        print(f"{self.i}  {self.j}   {self.k}")
        print(f"{num.i}  {num.j}   {num.k}")
        return (f"{self.i+num.i}i+{self.j+num.j}j+{self.k+num.k}k")



object=Parent(3, 6, 7)
object_2=Parent(5, 7, 9)

print(object)
print(object_2)

print(object+object_2)

        
