import os

def hide_files_and_folders(folder_path):
    # Use the attrib command to hide all files and subfolders in the folder
    os.system(f'attrib -h "{folder_path}\\*" /s /d')
    

if __name__ == "__main__":
    # Specify the folder path where you want to hide files and subfolders
    folder_path = 'E:\Lock.encrypted'

    # Check if the specified folder exists
    if os.path.exists(folder_path):
        hide_files_and_folders(folder_path)
        print(f'All files and subfolders in "{folder_path}" are now hidden.')
    else:
        print(f'Error: The folder "{folder_path}" does not exist.')
