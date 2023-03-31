def large_number(list):
    output=max(list)
    return print(f"The Value Of Maximum Number is {output}\n")

list=[]

for i in range(3):
    user=int(input(f"Enter The {i+1} Number\n"))
    list.insert(i,user)

large_number(list)
