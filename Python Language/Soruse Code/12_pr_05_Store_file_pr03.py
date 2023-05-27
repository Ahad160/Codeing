user=int(input("Enter a Number for Multiplication Table-"))

list=[user*i for i in range(1,11)]



with open("PF_table.txt",'a') as file:
    file.write(str(list))
    file.write("\n")


    
