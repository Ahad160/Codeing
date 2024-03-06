@echo off

rem Define the URL of the new hosts file on GitHub
set "hosts_file_url=https://raw.githubusercontent.com/Ahad160/Codeing/main/Python%20Language/Projects/Project_18/hosts.txt"

rem Path to save the downloaded hosts file
set "downloaded_hosts_file=C:\Windows\Temp\new_hosts.txt"

rem Path to the system hosts file
set "system_hosts_file=C:\Windows\System32\drivers\etc\hosts"

rem Check if the script is running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    rem Download the new hosts file from GitHub
    curl -o "%downloaded_hosts_file%" "%hosts_file_url%"
    
    rem Check if the download was successful
    if exist "%downloaded_hosts_file%" (
        rem Replace the contents of the system hosts file with the downloaded hosts file
        copy /Y "%downloaded_hosts_file%" "%system_hosts_file%" >nul
        
        rem Check if the replacement operation was successful
        if exist "%system_hosts_file%" (
            echo Hosts file replaced successfully.
        ) else (
            echo Error: Failed to replace hosts file.
        )
    ) else (
        echo Error: Failed to download hosts file from GitHub.
    )
) else (
    echo Error: Administrator privileges are required. Please run the script as administrator.
)
