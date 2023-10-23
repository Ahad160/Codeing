import ctypes
import os
import sys

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True  # The script is already running with admin privileges.
    else:
        # Re-run the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        return False

if run_as_admin():
    pass
else:
    sys.exit(0)  # Exit the script if not running with admin privileges.
