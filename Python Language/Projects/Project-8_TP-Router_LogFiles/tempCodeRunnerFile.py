#Log Files Analings
file_path = "E:\Router_Logfile.txt"


import re

# Define the target MAC address
target_mac = "E2:A3:6C:DD:EC:FE"

# Read the log file
with open(file_path, "r") as file:
    log_lines = file.readlines()

# Regular expression pattern to match lines with the target MAC address
pattern = r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}).*Recv REQUEST from {}\s+".format(re.escape(target_mac))

# Find and print lines matching the pattern
for line in log_lines:
    match = re.search(pattern, line)
    if match:
        date_time = match.group(1)
        print("Date and Time:", date_time)