user=int(input("Enter The Number\n"))
      
call = True
for i in range(2,user):
    if user%i==0:
        call=False
        break

if call:
    print(f"{user} is prime\n")
else:
    print(f"{user} is not prime\n")    

