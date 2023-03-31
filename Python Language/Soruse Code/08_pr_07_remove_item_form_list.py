str="Ahad Was a lier"

def remove(item):
    output=str.replace(item,"   ")

    return print(output.strip())

print(str)
user=(input("Enter The Word that You Wanted To Remove\n"))
remove(user)


