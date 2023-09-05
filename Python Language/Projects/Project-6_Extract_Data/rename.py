import os

folder_path = "E:\Bitten Tech Course\TechHacker Pre-Hacking Course\Module 3 (Linux Refresher) - Copy"  # Replace with the path to your folder
new_file_names = [
    "[3.1] Introduction to Command Line.mp4"
    "[3.2] Windows command line.mp4"
    "[3.3] Linux command line.mp4"
    "[3.4] Linux File System.mp4"
    "[3.5] NTFS vs FAT vs EXT.mp4"
    "[3.6] Linux User Administration.mp4"
    "[3.7] Basic DOS Commands.mp4"
    "[3.8] DOS Networking Commands.mp4"
    "[3.9] Kali 2019.4 and linux file system overview.mp4"
    "[3.10] Linux Elementary Commands.mp4"
    "[3.11] Linux Networking Commands.mp4"
    "[3.12] history and grep command.mp4"
    "[3.13] Working with Linux User Administration.mp4"
    "[3.14] Linux Working with Files, Permissions and Directories.mp4"
    "[3.15] Working with Linux File Permissions.mp4"
    "[3.16] Linux Working with Groups.mp4"
    "[3.17] Linux Package Manager apt.mp4"
    "[3.18] Linux Useful Files.mp4"

    # Add more new names as needed
]

if len(new_file_names) != 18:
    print("Error: You need to provide 18 new file names.")
else:
    files = os.listdir(folder_path)

    if len(files) != 18:
        print("Error: There are not 18 files in the folder.")
    else:
        for i in range(18):
            old_file_path = os.path.join(folder_path, files[i])
            new_file_path = os.path.join(folder_path, new_file_names[i])
            os.rename(old_file_path, new_file_path)

        print("Files renamed successfully.")
