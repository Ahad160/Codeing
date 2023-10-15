import Encryption_Folder
import Audio_Steganography


#Step-1
# Encryption_Folder.Encrypt()


#Step-2
message = "E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Project-14_Encrypting.key"  # Your message
with open(message, "r") as file:
    encrypted_key = file.read()
    
audio_file = "E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Music.mp3"  # Your input audio file
output_file = "E:\Codeing\Python Language\Projects\Project_14_Crypto_Stegano_Graphy\Music_With_Hidden_Message.wav"

Audio_Steganography.Embed_message(audio_file,encrypted_key,output_file)



