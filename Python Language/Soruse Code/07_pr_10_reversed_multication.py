user=int(input("Enter the number of multiplication table you want\n"))
print("Multiplication Table\n")


for i in range(1,11):
    s=10-i
    print(f"{user}X{s+1}={user*(s+1)}")