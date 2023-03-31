def shape(number):
    for i in range(number):
        output=print("*" * (number-i))
    return output


user=int(input("Enter The Size of Reverce Labber\n"))

shape(user)