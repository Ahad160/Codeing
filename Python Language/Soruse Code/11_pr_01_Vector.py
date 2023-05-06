class V2D:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
        
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"


class V3D(V2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"



object=V2D(2,6)

object2=V3D(9, 8, 1)


print(object)
print(object2)

