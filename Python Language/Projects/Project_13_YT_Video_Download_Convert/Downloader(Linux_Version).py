import pytube
from moviepy.editor import VideoFileClip
import os
import shutil
import argparse


print("""\033[33m
__   _______   _   _ _     _               ____  _________ _____  ______                    _                 _           
\ \ / /_   _| | | | (_)   | |             / /  \/  || ___ \____ | |  _  \                  | |               | |          
 \ V /  | |   | | | |_  __| | ___  ___   / /| .  . || |_/ /   / / | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  \ /   | |   | | | | |/ _` |/ _ \/ _ \ / / | |\/| ||  __/    \ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | |   | |   \ \_/ / | (_| |  __/ (_) / /  | |  | || |   .___/ / | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \_/   \_/    \___/|_|\__,_|\___|\___/_/   \_|  |_/\_|   \____/  |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                                                          
                                                                                                                          
\033[0m""")

print("Example: downloader--> -d -u https://www.youtube.com -cp C:/Users\PRO GADEGT/Videos/Captures")

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Download a file from a URL")

# Define the command-line arguments
parser.add_argument("-d", action="store_true", help="Download the file")
parser.add_argument("-u", type=str, help="URL to download from")
parser.add_argument("-cp", type=str, help="Custom Path to save the downloaded file")
parser.add_argument("-dp", action="store_true", help="Default Path to save the downloaded file")


# Prompt the user for the command line input
user=input("\033[34mDownloader->\033[0m ")

# Split the user input into a list of arguments
user_args = user.split()

# Parse the user-supplied command-line arguments
args = parser.parse_args(user_args)

# Check if the -d flag is provided to initiate the download
if args.d:
    if args.u:
        url = args.u

    Video_Intance=pytube.YouTube(url)
    steam=Video_Intance.streams.get_highest_resolution()

    if args.cp:
        path = args.cp
    
    if args.dp:
        path ='E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'

    steam.download(path)
    print(f"\033[32mDownloaded Is Completed And Save to: {path}\033[0m\n")  
else:
    print("Error: -d option is required to initiate the download.")


# if user==1:
#     # url=input("Enter URL:")
#     # Video_Intance=pytube.YouTube(url)
#     # steam=Video_Intance.streams.get_highest_resolution()
#     path=input("\033[32mDefult/Custom Path To Download [D/C]\033[0m")
#     if path=='D':
#         download_path = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'
#     elif path=='C':
#         path=input("\033[32mEnter Custom Path To Download\033[0m--")     
#         download_path = path
#     steam.download(output_path=download_path)
#     print("\033[31mYT Video Is Downloaded\033[0m\n")

# elif user==2:

#     url = input("Enter URL:")
#     video_instance = pytube.YouTube(url)
#     stream = video_instance.streams.get_highest_resolution()
#     downloaded_file = stream.download()

#     # Specify the custom paths for downloaded video and converted MP3
#     downloaded_video_path = 'E:\Codeing\Python Language\Projects\P-13'
#     converted_mp3_path = 'E:\Codeing\Python Language\Projects\P-13'

#     # Create the full file paths
#     downloaded_video_file = os.path.join(downloaded_video_path, os.path.basename(downloaded_file))
#     output_mp3_file = os.path.join(converted_mp3_path, 'Converted.mp3')

#     # Move the downloaded file to the custom directory
#     shutil.move(downloaded_file, downloaded_video_file)

#     # Extract the audio from the downloaded video and save it as an MP3 file
#     video_clip = VideoFileClip(downloaded_video_file)
#     audio_clip = video_clip.audio

#     # Save the audio as an MP3 file in the custom directory
#     audio_clip.write_audiofile(output_mp3_file)

#     # Close the video and audio clips
#     video_clip.close()
#     audio_clip.close()

#     print(f"Video converted to MP3 and saved as '{output_mp3_file}'")

