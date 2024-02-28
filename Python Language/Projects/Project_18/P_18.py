import os
import sys
import ctypes
import shutil
from cryptography.fernet import Fernet

#Ask For Run As Administrator
def run_as_admin():
  
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        return False

if run_as_admin():
    
    def Replace_File(source_file, destination_file):
        with open(source_file, "r") as key_file:
            key = key_file.read()

        with open(destination_file, "w+") as key_file2:
            key2 = key_file2.write(key)
        

    def Decryption(DEC_Key,DEC_File,Host):
        with open(DEC_File, "r") as key_file:
            key = key_file.read()
            change=key.replace('"','')
        with open(DEC_File, "w") as key_file:
            key = key_file.write(change)

        key = DEC_Key
        cipher_suite = Fernet(key)

        # Read the encrypted text from the file
        with open(DEC_File, "rb") as file:
            encrypted_text = file.read()

        # Decrypt and print the original text
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()

        with open(Host, "w") as key_file:
            key = key_file.write(decrypted_text)
            

    # Decryption-Part
    hostfile=r"C:\Windows\system32\hosts"   
    Key=r"IvxcaSyCCP4EXgpwBeWrSzockvOiPtKhM1lz4cpkkYU="
    File=r"E:\Codeing\Python Language\Projects\Project_18\hosts.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    Source_File= 'hosts.txt'
    File= os.path.join(script_dir, Source_File)
    Destination= r"C:\Windows\System32\drivers\etc\hosts"  # Replace with your destination file path

    Decryption(Key,File,hostfile)
    Replace_File(hostfile,Destination)

