list=[]

for i in range(0,4):
     a = int(input(f"Enter The {i+1} Number\n"))
     list.insert(i,a)


# # print("The Greatest Number is",max(list)) #For easy way

if list[0] > list[1] and list[0] > list[2] and list[0] > list[3]:
    print("The gratest number is",list[0])
elif list[1] > list[0] and list[1] > list[2] and list[1] > list[3]:
    print("The gratest number is",list[1])
elif list[2] > list[0] and list[2] > list[1] and list[2] > list[3]:
    print("The gratest number is",list[2])
else:print("The gratest number is",list[3])    


