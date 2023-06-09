def Functions(num):
    if num>20:
        return True
    else:
        return False

list_1=[1,34,56,57,32,66]


print(list(filter(Functions, list_1)))
