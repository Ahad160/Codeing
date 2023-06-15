from functools import reduce
Functions=lambda Num1,Num2 : max(Num1,Num2)

list=[31,10,23,60,70,40,888]

val=reduce(Functions,list)
print(f"The Maximum Number is {val}")


#Harry Vai Ways
Max=reduce(max,list)
print(Max)