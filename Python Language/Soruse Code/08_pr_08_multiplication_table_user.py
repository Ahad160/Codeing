def multiplication(number):
    for i in range(1,11):
        output=print(f"{number}X{i}={number*i}")
    return output

user=int(input("Enter The Number of Muliplication Table\n"))


multiplication(user)