while(True):
    
    try:
     user=(int(input("Enter The Number-"))) 
     print(user)


    except Exception as error:
        print(f"The user enter the wrong number so is showing {error}")