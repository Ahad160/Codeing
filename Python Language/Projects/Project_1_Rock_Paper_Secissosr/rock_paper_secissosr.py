import random

def logic(computer,user):
    if computer == user:
        return None        
    elif computer == 'Rock':
        if user == 'P':
            return True
        elif user == 'S':
            return False
    elif computer == 'Paper':
        if user == 'R':
            return False
        elif user == 'S':
            return True
    elif computer == 'Secissosr':
        if user == 'R':
            return True
        elif user == 'P':
            return False           


computer=random.randint(1, 3) #For random number generate

print("Computer Selecting Rock-(R) , Paper-(P), Secissosr-(S)\n")
if computer == 1:
    computer = 'Rock'
elif computer == 2:
    computer = 'Paper'
elif computer == 3:
    computer = 'Secissosr'

user=input("For Select Rock-(R) , Paper-(P), Secissosr-(S)\n")

result=logic(computer,user)



if user == 'R':
    user="Rock"
elif user == 'P':
    user = "Paper"
elif user == 'S':
    user = "Secissosr"      

print(f"Computer Chosse {computer}\n")
print(f"You Chosse {user}\n")

if result== None:
    print("This is Tie\n")
elif result:
    print("You Win😃\n")
else:
    print("You Lose😞\n")