$IP = getIP
$USER = $env:USERNAME
$HostName = $env:COMPUTERNAME
$Version = (Get-Host).Version.Major
$DATE = Get-Date -UFormat "%A %B %d, %Y"
$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HostName. Powershell version $Version. Today's Date is $DATE."
Send-MailMessage -To "johnjohnjohn109@gmail.com" -From "johnjohnjohn109@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
Write-Host("Email Sent")