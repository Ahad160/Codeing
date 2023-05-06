class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,sec):

        return Complex(self.real+sec.real,self.imaginary+sec.imaginary)

    def __mul__(self,sec):
        mulre= self.real*sec.real-self.imaginary*sec.imaginary
        mulim= self.real*sec.imaginary+self.imaginary*sec.real

        return complex(mulre,mulim)

    def __str__(self):
        return f'{self.real} + {self.imaginary}'


object=complex(1,4)

object_1=complex(8,5)


print(object+object_1)
print(object*object_1)
