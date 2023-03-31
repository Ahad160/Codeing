list=['donkey','mad','asshole']

with open("poem.txt","r") as file:
    reading=file.read()

for word in list:
    with open("poem.txt","w") as file:   
        file.write(reading.replace(word, "#######"))