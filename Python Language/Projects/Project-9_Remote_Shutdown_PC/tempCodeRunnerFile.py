import getpass
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

username = getpass.getuser()

print(f"Current User's Username: {username}")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
