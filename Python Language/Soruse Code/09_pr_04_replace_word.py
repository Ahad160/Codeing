file=open("poem.txt","r")

read=file.read()


if "Donkey" in read:
    file.close()
    file=open("poem.txt","w")
    file.write(read.replace("Donkey","######"))
    file.close()
else:
    print("The word 'Donkey did not present in poem.txt\n")    


