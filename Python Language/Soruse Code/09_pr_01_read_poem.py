file=open("poem.txt",'r')

reading=file.read()

if "turnrle" in reading:
    print("The word 'turnrle' is present this Poem\n")

print(reading)