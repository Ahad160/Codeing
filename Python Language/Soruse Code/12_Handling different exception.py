try:
    user=int(input("Enter A Number: "))
    divie=1/user
    print(divie)


except ValueError as error:
    print("Pleace Check Value")

except ZeroDivisionError as error:
    print("Division Error")    

except Exception as error:
    print('Primary Error')