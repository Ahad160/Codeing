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
