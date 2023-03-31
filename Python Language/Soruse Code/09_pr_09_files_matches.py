file=open("log.txt","r")

read=file.read()

file2=open("copy.txt",'r')

read2=file2.read()

if read == read2 :
    print("2 files content matches\n")
else :
    print("This 2 files content did not matches\n")    