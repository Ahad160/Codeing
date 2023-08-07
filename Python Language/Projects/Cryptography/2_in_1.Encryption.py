from cryptography.fernet import Fernet

# Read the encryption key from the key file
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Read the encrypted text from the file
with open("string.txt", "rb") as file:
    encrypted_text = file.read()

# Decrypt and print the original text
decrypted_text = cipher_suite.decrypt(encrypted_text).decode()

print("Decrypted Text:", decrypted_text)
user=input("Enter Some Text--")

file=open("string.txt",'w')
file.write(user)
file.close()

from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

file=open("string.txt",'r')
read=file.read()

# Input text
txt = read
file.close()

# Encrypt the text
encrypted_text = cipher_suite.encrypt(txt.encode())

# Save the encrypted text to a file
with open("string.txt", "wb") as file:
    file.write(encrypted_text)

# Save the key to a file (keep this key secret for decryption)
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)





dic={}

dic["hello"] = "asdsad"

print(dic)