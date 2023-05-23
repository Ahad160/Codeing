list=[123,2.4,True,'Raiden']

#Boring Way to Exprace Index
# index=0
# for item in list:
#     print(item,index)
#     index+=1

for index,item in enumerate(list):
    print(f'Item Name-{item} Index-{index}') 