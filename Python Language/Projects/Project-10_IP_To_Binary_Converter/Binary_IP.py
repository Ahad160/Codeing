
def Binary_IP(user):

    # User = []
    Full_IP = []

    # for a in range(0, 4):
    #     b = input(f"Enter {a + 1}st 8 Bits Of Binary: ")
    #     User.append(b)

    for a in range(0, 4):
        if len(user[a]) == 8:
            binary = []

            for char in user[a]:
                try:
                    binary.append(int(char))
                except ValueError:
                    print(f"Invalid input: '{char}' is not an integer.")
                    exit()

            Sum = 0
            for a in range(len(binary)):
                Sum += 2 ** (7 - a) * binary[a]  # Convert binary to decimal

            Full_IP.append(Sum)
        else:
            print("Please enter exactly 8 characters (integers).")

    # print("IP Address:", ".".join(map(str, Full_IP))) #Original

    # #TO Print in Yellow
    ip_address_str = ".".join(map(str, Full_IP))
    yellow_color_code = "\033[93m"
    reset_color_code = "\033[0m"
    formatted_output = f"IP Address: {yellow_color_code}{ip_address_str}{reset_color_code}"
    print(formatted_output)
