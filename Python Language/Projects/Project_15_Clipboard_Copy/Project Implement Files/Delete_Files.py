# File Delete
import os

File_Path=r"E:\Codeing\Python Language\Projects\Project_15_Clipboard_Copy\TEST_Delete_file.py"
os.remove(File_Path)

# Path Finder
import os
import sys

# Get the path of the script or executable
script_path = sys.argv[0]
# Get the absolute path of the script or executable
absolute_path = os.path.abspath(script_path)

print(f"The absolute path of the script or executable is: {absolute_path}")
