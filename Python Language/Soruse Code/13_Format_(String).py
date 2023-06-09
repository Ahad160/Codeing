# Hobby='Cyber Assaassin'
# A=f"Raiden Hobby is {Hobby}"
# print(A)

#Before f_Srting Comed

Hobby='Cyber Assaassin'
Real_Name="Raiden"
Age=19

A="Raiden Hobby is {}".format(Hobby)  #Syntax of Format
print(A)

B="{} Hobby is {} And Age is {}".format(Real_Name,Hobby,Age) #By Adding parameter order  {Read_name is 1st and hobby is 2nd .....}
print(B)

C="{2} Hobby is {1} And Age is {0}".format(Hobby,Real_Name,Age) #By Adding index in string as parameter
print(C)

