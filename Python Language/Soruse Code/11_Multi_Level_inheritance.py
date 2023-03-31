class Parents:
    Task="Study"
    Learn="Quran Sorif"

class Child_1(Parents):
    Play="Mobile Legends"
    # Learn="Youtube Videos"

class Child_2(Child_1):
    # Learn="Python"
    a=23



object=Child_2()


display=object.Learn

print(display)