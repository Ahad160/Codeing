file=open("log.txt","r")

read=file.read()

if "Python" in read:
    print("The Word Python Present in this file\n")
else:
    print("The word is not present in this file\n")    