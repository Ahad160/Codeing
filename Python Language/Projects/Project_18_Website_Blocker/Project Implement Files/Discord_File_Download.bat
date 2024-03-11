@echo off

rem Discord authentication token
set "token="

rem URL of the file attachment
set "attachment_url=https://cdn.discordapp.com/attachments/1215230567352639518/1215230672365690920/hosts?ex=65fbfec2&is=65e989c2&hm=a110a80acc6242ddeaa29ffb3e29fc178b4eff7a7c2b31129b695de35030bc66&"

rem Path to save the downloaded file
set "downloaded_file=file_name.txt"

rem Download the file using cURL
curl -H "Authorization: Bot %token%" -o "%downloaded_file%" "%attachment_url%"

rem Check if the download was successful
if exist "%downloaded_file%" (
    echo File downloaded successfully.
) else (
    echo Error: Failed to download file.
)

