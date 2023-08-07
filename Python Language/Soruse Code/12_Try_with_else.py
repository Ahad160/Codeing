try:
    user=int(input("Enter a Desemal:"))
    divide=1/user
except Exception as Error:
    print(Error)
else:
    print("The divide is sucessfully Complete")