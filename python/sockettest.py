import socket

try:
    hostname = str(sys.argv[1])
    ip = socket.gethostbyname(hostname)
    print(hostname + "has an IP of " + ip)
except:
    print("Oops, something is wrong with that host.")
host = ["www.uc.edu", "www.google.com", "www.reddit.com"]
print("working from host: " + socket.fqdn())
for h in host:
    gethostbyname(h)