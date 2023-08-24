
#Log Files Analings
file_path = "E:\Router_Logfile.txt"

import re
from datetime import datetime

# Define the target MAC address
target_mac = "EE:16:69:E1:50:24"

# Read the log file
with open(file_path, "r") as file:
    log_lines = file.readlines()

# Regular expression pattern to match lines with the target MAC address
pattern = rf"(\d{{4}}-\d{{2}}-\d{{2}}\s+\d{{2}}:\d{{2}}:\d{{2}}).*Recv REQUEST from {re.escape(target_mac)}\s+"

# Find and print lines matching the pattern
print("The List Of Date,Times when the client was Connected to the Router")
for line in log_lines:
    match = re.search(pattern, line)
    if match:
        date_time_str = match.group(1)
        date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        formatted_date_time = date_time_obj.strftime("%Y-%m-%d %I:%M:%S %p")
        print("Date and Time:", formatted_date_time)