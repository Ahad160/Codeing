import ast
import os
import psutil


class Storage:

    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2

    def ViewPassword(self):
        # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
        from cryptography.fernet import Fernet
        # Read the encryption key from the key file
        with open(self.path2, "rb") as key_file:
            key = key_file.read()

        cipher_suite = Fernet(key)

        # Read the encrypted text from the file
        with open(self.path1, "rb") as file:
            encrypted_text = file.read()

        # Decrypt and print the original text
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 

        #Convert String To Dict
        dictionary = ast.literal_eval(decrypted_text)

        print("\n🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
        for key, value in dictionary.items():
            print(f"{key} - {value}")
        print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨\n")

        Back = input("Press Any Button To Continue--")

    def EditPassword(self):
        # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
        from cryptography.fernet import Fernet
        # Read the encryption key from the key file
        with open(self.path2, "rb") as key_file:
            key = key_file.read()

        cipher_suite = Fernet(key)

        # Read the encrypted text from the file
        with open(self.path1, "rb") as file:
            encrypted_text = file.read()

        # Decrypt and print the original text
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓   

        with open(self.path1,"w") as file:
            file.write(decrypted_text)

        with open(self.path1, "r+") as file:
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

                # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
                from cryptography.fernet import Fernet

                # Generate a random encryption key
                key = Fernet.generate_key()
                cipher_suite = Fernet(key)


                file = open(self.path1, 'r')
                read = file.read()

                # Input text
                txt = read
                file.close()

                # Encrypt the text
                encrypted_text = cipher_suite.encrypt(txt.encode())

                # Save the encrypted text to a file
                with open(self.path1, "wb") as file:
                    file.write(encrypted_text)

                # Save the key to a file (keep this key secret for decryption)
                with open(self.path2, "wb") as key_file:
                    key_file.write(key)
                # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption


            else:
                print("Incorrect Account Name\n")

    def AddPassword(self):

        dict_Key = input("Enter Account Name➡️   ")
        value = input(f"Enter {dict_Key} Password➡️   ")

        # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
        from cryptography.fernet import Fernet
        # Read the encryption key from the key file
        with open(self.path2, "rb") as key_file:
            key = key_file.read()

        cipher_suite = Fernet(key)

        # Read the encrypted text from the file
        with open(self.path1, "rb") as file:
            encrypted_text = file.read()

        # Decrypt and print the original text
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓

        #Convert String To Dict
        dictionary = ast.literal_eval(decrypted_text)

        dictionary[dict_Key] = value

        sread = open(self.path1, "w")
        sread.write(str(dictionary))
        sread.truncate()

        # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
        from cryptography.fernet import Fernet

        # Generate a random encryption key
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)


        file = open(self.path1, 'r')
        read = file.read()

        # Input text
        txt = read
        file.close()

        # Encrypt the text
        encrypted_text = cipher_suite.encrypt(txt.encode())

        # Save the encrypted text to a file
        with open(self.path1, "wb") as file:
            file.write(encrypted_text)

        # Save the key to a file (keep this key secret for decryption)
        with open(self.path2, "wb") as key_file:
            key_file.write(key)
        # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption

    def RemovePassword(self):
        try:
            # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
            from cryptography.fernet import Fernet
            # Read the encryption key from the key file
            with open(self.path2, "rb") as key_file:
                key = key_file.read()

            cipher_suite = Fernet(key)

            # Read the encrypted text from the file
            with open(self.path1, "rb") as file:
                encrypted_text = file.read()

            # Decrypt and print the original text
            decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
            # 🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓

            dictionary = ast.literal_eval(decrypted_text)
            lists = list(dictionary.keys())

            for i in range(len(lists)):
                print(f"{i+1}.{lists[i]}")

            dict_key = input("Enter Account Name➡️   ")

            del dictionary[dict_key]

            print(f"🔴 {dict_key} Password is Deleted🔴\n")

            sread = open(self.path1, "w")
            sread.write(str(dictionary))
            sread.truncate()

            # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
            from cryptography.fernet import Fernet

            # Generate a random encryption key
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)


            file = open(self.path1, 'r')
            read = file.read()

            # Input text
            txt = read
            file.close()

            # Encrypt the text
            encrypted_text = cipher_suite.encrypt(txt.encode())

            # Save the encrypted text to a file
            with open(self.path1, "wb") as file:
                file.write(encrypted_text)

            # Save the key to a file (keep this key secret for decryption)
            with open(self.path2, "wb") as key_file:
                key_file.write(key)
            # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption


        except Exception as error:
            print("Incorrect Account Name\n")


# Auto Startup Check

# To Check A File
def list_drive_letters():
    drive_letters = set()
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.device and partition.mountpoint:
            drive_letter = partition.device[0].upper() + ":"
            drive_letters.add(drive_letter)

    return sorted(drive_letters)


drive_letters = list_drive_letters()

file_path = f"{drive_letters[1]}\Database.txt"
file_path_2 = f"{drive_letters[1]}\encryption_key.key"

# To Create The File
if os.path.exists(file_path):
    pass
else:
    data = {}
    with open(file_path, 'w') as file:
        file.write(str(data))

    # Encryption-----Auto
    from cryptography.fernet import Fernet
    # Generate a random encryption key
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    with open(file_path, "r") as file:
        read = file.read()

    # Input text
    txt = read

    # Encrypt the text
    encrypted_text = cipher_suite.encrypt(txt.encode())

    # Save the encrypted text to a file
    with open(file_path, "wb") as file:
        file.write(encrypted_text)

    # Save the key to a file (keep this key secret for decryption)
    with open(file_path_2, "wb") as key_file:
        key_file.write(key)


object = Storage(file_path, file_path_2)


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
