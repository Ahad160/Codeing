import ctypes
import os
import sys

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
sys.exit(0)  # Exit the script if not running with admin privileges.
