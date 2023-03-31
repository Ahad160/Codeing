for i in range(2,5):
    file=open(f"{i}_table.txt","w")
    for j in range(1,11):      
        file.write((f"{i}X{j}={i*j}\n"))


