import os
import win32net
import win32netcon
import getpass
import socket

# Make a Folder
folder_path = "C:\XboxGames_Logs"
os.makedirs(folder_path)
print("File is Created")


folder_name = "XboxGames_Logs"
folder_path = r"C:\XboxGames_Logs"

share_info = {
    'netname': folder_name,
    'path': folder_path,
    'remark': 'Shared folder description',
    'permissions': win32netcon.ACCESS_ALL,
    'max_uses': -1,  # -1 allows unlimited access
    'current_uses': 0,
}

try:
    win32net.NetShareAdd(None, 2, share_info)
    print(f"Folder '{folder_name}' File is  shared successfully.")
except Exception as e:
    print(f"Error: {e}")


# For User IP,Name
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

username = getpass.getuser()

print(f"Current User's Username: {username}")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


input("Press Enter to exit...")

