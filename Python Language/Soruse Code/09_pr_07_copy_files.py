file=open("log.txt",'r')

read=file.read()

copyfile=open("copy.txt",'w')

copyfile.write(read)

file.close()
copyfile.close()