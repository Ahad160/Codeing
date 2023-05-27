try:
    user1=int(input("Enter the value of (A)-"))
    user2=int(input("Enter the value of (B)-"))

    print(user1/user2)


except ZeroDivisionError as error:
    print("Infinite By Handing The ZeroDivisionError")