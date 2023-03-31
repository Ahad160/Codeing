user=int(input("Enter the number of multiplication table you want\n"))
print("Multiplication Table")

i=1
while i<11:
    print(f"{user}X{i}={user*i}")
    i=i+1