from yt_dlp import YoutubeDL

try:

    User = input("Enter the Youtube Video link- ")
    Path = input("\nEnter the Download Folder Path- ")

    options = {
        'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',  # Best 4K or lower
        'outtmpl': rf'{Path}/4kfile.%(ext)s',

    }

    with YoutubeDL(options) as ydl:
        ydl.download([User])

except Exception as e:
    exit()
