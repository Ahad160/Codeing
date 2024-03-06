@echo off

rem Define the URL of the hosts file on GitHub
set "hosts_file_url=https://raw.githubusercontent.com/Ahad160/Codeing/main/Python%20Language/Projects/Project_18/hosts"

rem Path to the temporary hosts file
set "temp_hosts_file=%TEMP%\hosts"

rem Path to the system hosts file
set "system_hosts_file=C:\Windows\System32\drivers\etc\hosts"

rem Check if the script is running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    rem Download the hosts file from GitHub using curl
    curl -o "%temp_hosts_file%" "%hosts_file_url%"
    
    rem Check if the download was successful
    if exist "%temp_hosts_file%" (
        rem Replace the system hosts file with the temporary hosts file
        copy /Y "%temp_hosts_file%" "%system_hosts_file%"
        
        rem Check if the replacement was successful
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
