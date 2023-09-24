import random

# Function to convert Arabic numerals to Bengali numerals
def arabic_to_bengali(number):
    bengali_digits = {
        '0': '০',
        '1': '১',
        '2': '২',
        '3': '৩',
        '4': '৪',
        '5': '৫',
        '6': '৬',
        '7': '৭',
        '8': '৮',
        '9': '৯',
    }
    return ''.join([bengali_digits[digit] for digit in str(number)])

# Defined paths For A_1
input_file_path = r"E:\Codeing\Python Language\Projects\Project-11_Question_Generator\Subjects\Java Programming\A_1.txt"
# Defined paths For S_1
input_file_path2 = r"E:\Codeing\Python Language\Projects\Project-11_Question_Generator\Subjects\Java Programming\S_1.txt"
# Defined paths For R_1
input_file_path3 = r"E:\Codeing\Python Language\Projects\Project-11_Question_Generator\Subjects\Java Programming\R_1.txt"
# Defined paths For Question_Paper(GEN).txt
output_file_path = "Question_Paper(GEN).txt"

#//A_1
# Create an empty list to store the random texts
random_texts = []

# Generate 5 random numbers

random_numbers = random.sample(range(1, 39),5)

# Read the corresponding lines from the input file and add Bengali numbering
for i, num in enumerate(random_numbers, start=1):
    with open(input_file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        if num <= len(lines):
            bengali_text = lines[num - 1].strip()
            bengali_number = arabic_to_bengali(i)  # Convert the index to Bengali
            random_texts.append(f"{bengali_number}. {bengali_text}")

# Join the random texts into a single string
random_text = "\n".join(random_texts)

#Intro Text
with open(output_file_path, "w", encoding="UTF-8") as output_file:
    output_file.write("\t\t\t\tডিপ্লোমা-ইন-ইঞ্জিনিয়ারিং\n\t\t\t\tবিষয় : জাভা প্রোগ্রামিং\n\t\t\t\t(কোডঃ ২৮৫৪১)\n\n")

# Write the header to the output file
with open(output_file_path, "a", encoding="UTF-8") as output_file:
    output_file.write("\t\t(ক ও খ বিভাগের সকল প্রশ্নের এবং গ বিভাগের যেকোন ২টি প্রশ্নের উত্তর দাও)\n\t\t\t\tক বিভাগ (মান: ১ X ৫ = ৫)\n\n")

# Append the random texts to the output file
with open(output_file_path, "a", encoding="UTF-8") as output_file:
    output_file.write(random_text)



#//S_1
# Create an empty list to store the random texts
random_texts = []

# Generate 5 random numbers
random_numbers = random.sample(range(1, 26),3)

# Read the corresponding lines from the input file and add Bengali numbering
for i, num in enumerate(random_numbers, start=1):
    with open(input_file_path2, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        if num <= len(lines):
            bengali_text = lines[num - 1].strip()
            bengali_number = arabic_to_bengali(i+5)  # Convert the index to Bengali
            random_texts.append(f"{bengali_number}. {bengali_text}")

# Join the random texts into a single string
random_text = "\n".join(random_texts)

# Write the header to the output file
with open(output_file_path, "a", encoding="UTF-8") as output_file:
    output_file.write("\n\n\t\t\t\tখ বিভাগ (মান: ২ X ৩ = ৬) \n\n")
 

# Append the random texts to the output file
with open(output_file_path, "a", encoding="UTF-8") as output_file:
    output_file.write(random_text)




#//R_1
# Create an empty list to store the random texts
random_texts = []

# Generate 5 random numbers
random_numbers = random.sample(range(1, 7),3)

# Read the corresponding lines from the input file and add Bengali numbering
for i, num in enumerate(random_numbers, start=1):
    with open(input_file_path3, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        if num <= len(lines):
            bengali_text = lines[num - 1].strip()
            bengali_number = arabic_to_bengali(i+8)  # Convert the index to Bengali
            random_texts.append(f"{bengali_number}. {bengali_text}")

# Join the random texts into a single string
random_text = "\n".join(random_texts)

# Write the header to the output file
with open(output_file_path, "a", encoding="UTF-8") as output_file:
    output_file.write("\n\n\t\t\t\tগ বিভাগ (মান : ৪.৫ x ২ = ১) \n\n")
     
 

# Append the random texts to the output file
with open(output_file_path, "a", encoding="UTF-8") as output_file:
    output_file.write(random_text)