from functools import reduce
Fun=lambda Num1,Num2 :Num1*Num2

list=[1,2,3,4,5]

Val=reduce(Fun,list)

print(Val)

#The Principal of reduce
# list=[1,2,3,4,5]
#     (1 + 2)  3  4  5
#       (3 + 3)   4
#         (6 + 4)
#            10
