#Method-1
def Sequre(num):
    return num*num

list_1=[1,2,3,4,5]
list_2=[]

for item in list_1:
    list_2.append(Sequre(item))

print(list_2)

#Method-2

print(list(map(Sequre,list_1)))