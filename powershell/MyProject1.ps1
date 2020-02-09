#What it does: This is a script that clears the cache from Chrome
#Output: You should see each cache being deleted because of -Verbose. And "Google Chrome Cache Removal - COMPLETE" to let you know the script is done.
#How to run it: To run it copy the script into your own powershell and run it. To check if the script worked check the file path "C:\Users\YourUser\AppData\Local\Google\Chrome\User Data\Default\Cache\*". The cache file should be empty.
Remove-Item -path "C:\Users\$env:USERNAME\AppData\Local\Google\Chrome\User Data\Default\Cache\*" -Recurse -Force -EA SilentlyContinue -Verbose
Write-Host "Google Chrome Cache Removal - COMPLETE"