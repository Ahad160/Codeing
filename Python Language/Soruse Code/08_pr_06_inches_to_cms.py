def converter(number):
    output=number*2.54
    return output

print("🔴inches To cm Converter🔴")
user=int(input("Enter inches\n"))

print(f"{user} inches is {converter(user)} cm")