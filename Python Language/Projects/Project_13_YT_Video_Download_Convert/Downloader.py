import pytube
from moviepy.editor import VideoFileClip
import os
import shutil

user=int(input("1.Download Youtube Video\n2.Convert YT Video To MP3 And Download\nSelect-"))

if user==1:
    url=input("Enter URL:")
    Video_Intance=pytube.YouTube(url)
    steam=Video_Intance.streams.get_highest_resolution()
    download_path = 'E:\Codeing\Python Language\Projects\P-13'
    steam.download(output_path=download_path)

elif user==2:

    url = input("Enter URL:")
    video_instance = pytube.YouTube(url)
    stream = video_instance.streams.get_highest_resolution()
    downloaded_file = stream.download()

    # Specify the custom paths for downloaded video and converted MP3
    downloaded_video_path = 'E:\Codeing\Python Language\Projects\P-13'
    converted_mp3_path = 'E:\Codeing\Python Language\Projects\P-13'

    # Create the full file paths
    downloaded_video_file = os.path.join(downloaded_video_path, os.path.basename(downloaded_file))
    output_mp3_file = os.path.join(converted_mp3_path, 'Converted.mp3')

    # Move the downloaded file to the custom directory
    shutil.move(downloaded_file, downloaded_video_file)

    # Extract the audio from the downloaded video and save it as an MP3 file
    video_clip = VideoFileClip(downloaded_video_file)
    audio_clip = video_clip.audio

    # Save the audio as an MP3 file in the custom directory
    audio_clip.write_audiofile(output_mp3_file)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

    print(f"Video converted to MP3 and saved as '{output_mp3_file}'")

