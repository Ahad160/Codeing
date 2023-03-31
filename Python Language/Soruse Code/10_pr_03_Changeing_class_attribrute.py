class Change:
    a=500
    b=300


object=Change()

print(object.a) #Before
object.a=0

print(object.a) #After
print(object.b)
