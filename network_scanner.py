import socket
import sys
from datetime import datetime

# Target definition
target = "127.0.0.1" # Can be changed to any target IP

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

ports = [21, 22, 23, 25, 80, 110, 443, 8080]

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting Script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname Could Not Be Resolved.")
    sys.exit()

except socket.error:
    print("\nServer Not Responding.")
    sys.exit()
