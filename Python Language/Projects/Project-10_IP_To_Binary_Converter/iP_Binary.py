
def iP_Binary(user):

    bit_values = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_octets = []

    # user = input("Enter an IP address: ")

    ip = user.split(".")

    ip = [int(part) for part in ip]

    for b in range(len(ip)):
        On = []  # Initialize On list for each octet
        for a in range(len(bit_values)):
            c = ip[b] - bit_values[a]
            if c < 0:
                On.append('0')
            else:
                On.append('1')
                ip[b] = c
        binary_octets.append("".join(On))

    for i, binary_octet in enumerate(binary_octets):
        # print(f"Octet {i + 1} (Binary): {binary_octet}") #Original

        print(f"\033[93mOctet {i + 1} (Binary): {binary_octet}\033[0m") #Original






