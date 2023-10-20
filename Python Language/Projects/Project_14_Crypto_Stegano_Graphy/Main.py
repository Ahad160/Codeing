import Encryption_Folder
import Audio_Steganography
import Google_Drive_API
import os
import psutil

#Define Path For Aceess
Main_File_Path=r'E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\User_Data'
Steganography_Audio = "E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Music.mp3"  # Your input audio file
Steganography_Audio_Output = "E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Music_With_Hidden_Message.wav"


#Step-1
Setp_1=Encryption_Folder.Encrypt(Main_File_Path)

Setp_2=Audio_Steganography.Embed_message(Steganography_Audio,Setp_1,Steganography_Audio_Output)

Google_Drive_API.Google_Drive_API(Setp_2)
