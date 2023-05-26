user=int(input("Enter a Number for Multiplication Table-"))

list_1=[]

for i in range(1,11):
    num=user*i
    list_1.append(num)
    
    list=[i for i in list_1 ]



with open("table.txt",'w') as file:
    file.write(str(list))


    
