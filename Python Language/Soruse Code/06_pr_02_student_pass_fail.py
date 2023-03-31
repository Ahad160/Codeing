list=[]

for i in range(1,4):
    a=int(input(f"Enter The {i} Subject Marks\n"))
    list.insert(i,a)

L1= sum(list)

if list[0] <33 or list[1] <33 or list[2] <33:
    print("Youer Fail in Exam\n")

elif (L1/3) <40 :
    print("You are fail due to total percentice is less than 40%\n")
else:print("Congatulation ! You Have Pass in this exam\n")






