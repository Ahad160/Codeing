import Binary_IP
import iP_Binary

print("\033[92m\tIP To Binary Converter\033[0m")
print("\033[91m-----------------------------------\033[0m")
print("\u001b[36m(1) Binary_TO_IP    (2) IP_TO_Binary\u001b[0m")
print("\033[91m-----------------------------------\033[0m")

user=(int(input("\n\tSelect-")))


if user == 1:
    User = []
    for a in range(0, 4):
        b = input(f"Enter {a + 1}st 8 Bits Of Binary: ")
        User.append(b)
    Binary_IP.Binary_IP(User) #Moudeling
elif user == 2:
    user = input("Enter an IP address: ")
    iP_Binary.iP_Binary(user)

