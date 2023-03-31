import os 

file=open("copy.txt","r")

read=file.read()

file2=open("Renamed_by_python.txt","w")

file2.write(read)

file.close()
file2.close()

os.remove("copy.txt")