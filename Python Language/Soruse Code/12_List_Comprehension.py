# list=[12,3,42,4,2,5,14,77]
# list2=[]
# for item in list:
#     if item%2==0:
#         list2.append(item)

# print(list2)        

#Shortcut Way
list=[12,3,42,4,2,5,14,77]

list2 = [i for i in list if i%2==0]

# Newlistvariable = [for variable for for variable in list condition]

print(list2)