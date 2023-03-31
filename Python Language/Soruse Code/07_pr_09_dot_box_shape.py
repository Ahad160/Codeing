n=3
for i in range(0,1):
    print("*" * n)
    for j in range(0,1):
        print("*" * (j+1),end="")
        print(" " ,end="")
        print("*" * (j+1))
    print("*" * n)  
    