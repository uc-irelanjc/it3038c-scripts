import os
filename = "/var/log/secure"

with open(filename) as f:
    line = set(f)