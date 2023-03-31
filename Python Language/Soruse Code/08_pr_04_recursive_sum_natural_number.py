def recursive(Number):
   
    if Number==0 or Number==1:
        return 1
    return Number + recursive(Number-1)

User=int(input("Enter The Number\n"))

print(recursive(User))