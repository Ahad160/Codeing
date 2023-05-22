A=23 # Its a Global Variable

def Variable():
    global A # Use the Global Variable
    print(A)
    A=33 # it is a  Local Variable
    print(A)
  


Variable()

print(A)



