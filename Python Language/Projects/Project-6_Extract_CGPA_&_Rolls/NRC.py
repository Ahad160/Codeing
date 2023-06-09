# Open file 1 containing board rolls
with open("ALL_Roll.txt","r") as f1:
    board_rolls = f1.readlines()

# Open file 2 containing board rolls and CGPA
with open("GAI_CGPA.txt", "r") as f2:
    board_cgpa = f2.readlines()

# Extract board rolls from file 1
board_rolls = [roll.strip() for roll in board_rolls]

# Open file 3 to write matching rolls and CGPA
with open("file3.txt", "w") as f3:
    # Iterate over board rolls and CGPA in file 2
    for line in board_cgpa:
        # Extract roll and CGPA (if available)
        values = line.strip().split()
        if len(values) > 0:
            roll = values[0]
            cgpa = values[1] if len(values) > 1 else None
            # If roll is in file 1, write it to file 3
            if roll in board_rolls:
                f3.write(f"{roll} {cgpa}\n")
                print(f"Copied {roll} {cgpa}")