import os
import psutil



#To Check A File
def list_drive_letters():
    drive_letters = set()
    partitions = psutil.disk_partitions(all=True)
    
    for partition in partitions:
        if partition.device and partition.mountpoint:
            drive_letter = partition.device[0].upper() + ":"
            drive_letters.add(drive_letter)
    
    return sorted(drive_letters)

drive_letters = list_drive_letters()


file_path = f"{drive_letters[1]}/Database.txt"

print(file_path)