file=open("log.txt","r")


for i in range(1,60):
    read=file.readline()
    if "Python" in read:
        print(read)
        