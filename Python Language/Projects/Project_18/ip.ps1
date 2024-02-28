# Define the domain and IP address
$domain = "example.com"
$ip_address = "127.0.0.1"

# Path to the hosts file
$hosts_file = "$env:SystemRoot\System32\drivers\etc\hosts"

# Check if the domain entry already exists in the hosts file
$existing_entry = Get-Content $hosts_file | Where-Object {$_ -like "*$domain*"}

# If the domain entry doesn't exist, add it to the hosts file
if (-not $existing_entry) {
    # Construct the entry to add
    $new_entry = "$ip_address`t$domain"

    # Append the new entry to the hosts file
    Add-Content -Path $hosts_file -Value $new_entry
    Write-Host "Domain '$domain' added to the hosts file."
} else {
    Write-Host "Domain '$domain' already exists in the hosts file."
}
