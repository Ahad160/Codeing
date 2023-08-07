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
