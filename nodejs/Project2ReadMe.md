For project 2 I added to the server.js script to allow it tp show the model of the cpu, type release and arch of OS, and the home directory of the computer. This is all in addition to what it already did.

To run this script copy the code into visual studio and type 'node server.js' to start the web server.

Next go to another computer on your network and access the webserver through a browser by searching "ipofcomputer:3000/sysinfo".

The webpage should display the following:

Hostname: irelanjc-win

IP: 192.168.33.165

Server Uptime: Days: 0, Hours 0, Minutes: 18, Seconds: 29

Total Memory: 4293.89824 MB

Free Memory: 1744.416768 MB

Model: Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz

Number of CPUs: 2

OS Info: Windows_NT / 10.0.17134 / x64

Home Directory: C:\Users\Administrator

If it does not work you may need to disable your firewalls and try it again.