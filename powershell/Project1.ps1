Remove-Item -path "C:\Users\$env:USERNAME\AppData\Local\Google\Chrome\User Data\Default\Cache\*" -Recurse -Force -EA SilentlyContinue -Verbose
Write-Host "Google Chrome Cache Removal - COMPLETE"