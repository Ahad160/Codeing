@echo off

rem Define the URL of the hosts file on GitHub
set "hosts_file_url=https://raw.githubusercontent.com/username/repository/branch/hosts"

rem Path to the system hosts file
set "system_hosts_file=C:\Windows\System32\drivers\etc\hosts"

rem Check if the script is running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    rem Download the hosts file from GitHub using curl
    curl -o "%system_hosts_file%" "%hosts_file_url%"
    
    rem Check if the download was successful
    if exist "%system_hosts_file%" (
        echo Hosts file replaced successfully.
    ) else (
        echo Error: Failed to replace hosts file.
    )
) else (
    echo Error: Administrator privileges are required. Please run the script as administrator.
)
