# Open file 1 containing board rolls and CGPA
with open("GAI_CGPA.txt", "r") as f1:
    board_cgpa = f1.readlines()

# Open file 2 containing names and board rolls
with open("ALL_Roll.txt", "r") as f2:
    board_names_rolls = f2.readlines()


# Create a dictionary to store rolls and corresponding names from file 2
roll_name_dict = {}
for line in board_names_rolls:
    values = line.strip().split()
    if len(values) >= 2:
        roll = values[1]
        name = values[0]
        roll_name_dict[roll] = name

# Open file 3 to write matching names, rolls, and CGPA
with open("file3.txt", "w") as f3:
    # Iterate over board rolls and CGPA in file 1
    for line in board_cgpa:
        # Extract roll and CGPA (if available)
        values = line.strip().split()
        if len(values) >= 2:
            roll = values[0]
            cgpa = values[1]
            # Search for roll in roll_name_dict
            if roll in roll_name_dict:
                name = roll_name_dict[roll]
                # Write name, roll, and CGPA to file 3
                f3.write(f"{name} {roll} {cgpa}\n")
            else:
                # Write "fail" if roll does not exist in file 2
                # f3.write(f"fail {roll} {cgpa}\n")
                pass
