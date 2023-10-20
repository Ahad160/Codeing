
import os
import psutil

# To Check A File
def list_drive_letters():
    drive_letters = set()
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.device and partition.mountpoint:
            drive_letter = partition.device[0].upper() + ":"
            drive_letters.add(drive_letter)

    return sorted(drive_letters)

drive_letters = list_drive_letters()

# Check if there is a second drive letter available
if len(drive_letters) > 1:
    drive_letter = drive_letters[1]

    # List folders on the specified drive
    drive_path = drive_letter + "/"
    if os.path.exists(drive_path) and os.path.isdir(drive_path):
        folder_names = [d for d in os.listdir(drive_path) if os.path.isdir(os.path.join(drive_path, d))]

        # Check if there are any folders
        if folder_names:
            # Get the first folder's path and create a file in it
            first_folder = folder_names[0]
            file_path = os.path.join(drive_path, first_folder, "my_file.txt")

            # Create and write to the file
            with open(file_path, 'w') as file:
                file.write("Hello it's a txt")
                print(f"Data written to {file_path}")
        else:
            print(f"No folders found on {drive_letter}.")
    else:
        print(f"The drive {drive_letter} does not exist or is not a valid directory.")
else:
    print("There is no second drive available.")
