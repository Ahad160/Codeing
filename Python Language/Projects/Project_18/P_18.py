import os
import sys
import ctypes
import shutil

#Ask For Run As Administrator
def run_as_admin():
  
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        return False

if run_as_admin():
    
    def Replace_File(source_file, destination_file):
        try:
            shutil.copy2(source_file, destination_file)  # Copy source file to destination file
            print(f"File '{source_file}' replaced successfully with '{destination_file}'.")
        except FileNotFoundError:
            print(f"Error: File '{source_file}' not found.")
        except PermissionError:
            print(f"Error: Permission denied while replacing file '{source_file}'.")

    Source= r"E:\Codeing\Python Language\Projects\Project_18\hosts.txt"  # Replace with your source file path
    Script_dir= os.path.dirname(os.path.abspath(__file__))
    Source_File= 'Hosts'
    Source= os.path.join(Script_dir, Source_File)
    Destination= r"C:\Windows\System32\drivers\etc\hosts"  # Replace with your destination file path

    Replace_File(Source,Destination)
