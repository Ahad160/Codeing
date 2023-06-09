import ast

class Storage:
    def ViewPassword(self):
        with open("viewpass.txt", "r") as file:
            read = file.read()
        dictionary = ast.literal_eval(read)

        print("\n🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
        for key, value in dictionary.items():
            print(f"{key} - {value}")
        print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨\n")

    def EditPassword(self):
        with open("viewpass.txt", "r+") as file:
            read = file.readlines()
            file.seek(0)

            dictionary = ast.literal_eval(read[0])
            lists = list(dictionary.keys())

            for i in range(len(lists)):
                print(f"{i+1}.{lists[i]}")

            key = input("Enter Account Number➡️   ")
            found = False

            for j in range(len(lists)):
                if key == lists[j]:
                    value = input(f"Enter New Password Of {key}➡️  ")
                    dictionary[key] = value
                    found = True
                    break
            if found:
                file.write(str(dictionary))
                file.truncate()
            else:
                print("Incorrect Account Name\n")

    def AddPassword(self):
        key=input("Enter Account Name➡️   ")
        value=input(f"Enter {key} Password➡️   ")

        file= open("viewpass.txt","r")
        read=file.read()

        dictionary = ast.literal_eval(read)
        dictionary[key] = value
        
        sread= open("viewpass.txt","w")
        sread.write(str(dictionary))
        sread.truncate()

    def RemovePassword(self):
        try:
            file= open("viewpass.txt","r")
            read=file.read()

            dictionary = ast.literal_eval(read)
            lists = list(dictionary.keys())

            for i in range(len(lists)):
                print(f"{i+1}.{lists[i]}")    

            key=input("Enter Account Name➡️   ")

            del dictionary[key]

            print(f"🔴 {key} Password is Deleted🔴\n")

            sread= open("viewpass.txt","w")
            sread.write(str(dictionary))
            sread.truncate()
        except  Exception as error:
                print("Incorrect Account Name\n")


object = Storage()

while True:
    try:
        print(" \t🟢\033[91mPassword Manager\033[0m🟢")
        print("""----------------------------------------
    🔺       1.View All Password          🔺
    🔺       2.Edit Password              🔺
    🔺       3.Add Password               🔺
    🔺       4.Delete Password            🔺
    🔺       5.Exit                       🔺
    ----------------------------------------""")
        user = int(input("Choose an option➡️   "))
        if user == 1:
            object.ViewPassword()
        elif user == 2:
            object.EditPassword()
        elif user == 3:
            object.AddPassword()
        elif user == 4:
            object.RemovePassword()
        elif user == 5:
            print("Closing Password Manager")
            exit()
        else:
            print("Invalid Choice!")

    except ValueError as error:
        print("Enter valid Choice")

