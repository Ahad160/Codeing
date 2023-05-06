class Vector:
    def __init__(self,list):
        self.list=list

    def __str__(self):
        str=""
        index=0
        for i in self.list:
            str += f"{i}_A_{index} + "
            index += 1     
        return str[:-1]

    def __add__(self,sec):  
        new_LIST= []
        for i in range(len(self.list)):
            new_LIST.append(self.list[i]+sec.list[i])
        return Vector(new_LIST)

    def __mul__(self,sec):
        Total=0
        for i in range(len(self.list)):
            Total += self.list[i] *sec.list[i]
        return Total   


object=Vector([2,3])
object_1=Vector([4,5])



print(object+object_1)
print(object*object_1)
