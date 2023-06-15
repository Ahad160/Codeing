def Function(num):
    num=str(num)
    if  num[-1]=="0" or num[-1]=="5":
        return True
    else:
        return False 
        
list_1=[125,232,653,745,450,753,550]

print(list(filter(Function,list_1)))



#Harry Vai Ways
sec=list(filter(lambda i:i%5==0,list_1))

print(sec)
  