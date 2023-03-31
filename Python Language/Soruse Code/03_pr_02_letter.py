# print('''       Dear <Name
#                   You are Selected!
#                   <Date>  ''')

# user1=input("Name-")
# user2=input("Date-")

# print("\tDear ",user1)
# print("\t \t You are Selected!")
# print("\t\t",user2)

letter=('''       Dear <Name>
                  You are Selected!
                  <Date>  ''')

print(letter)

name=input("Enter youer name\n")
date=input("Enter youer date\n")

letter=letter.replace("Name",name)
letter=letter.replace("Date",date)

print(letter)





