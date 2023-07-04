list=[1,2,3,4,5,6,7,8,9,0]

It=iter(list)

# print(next(It)) #For print one item only

#For print the full list
try:
    while True:
        print(next(It))
except StopIteration as i:
    pass          