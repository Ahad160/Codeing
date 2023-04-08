class Parent:
    code=98098
    def __str__(self):
     return f"Code is {self.code}"

class Child:
    lenth="900"
    def __len__(self):
        return 500

object=Parent()
object_2=Child()


print(object)
print(len(object_2))
