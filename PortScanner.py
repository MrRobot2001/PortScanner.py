import sys
import socket 
from datetime import datetime

#define the target
if len(sys.argv) == 2:
   Target = socket.gethostbyname(sys.argv[1])#translating Hostname to IPV4
else:
   print('INvalid length of arguments')
   print('Syntax: python3 PortScanner.py <ip>')

print('*' * 20)
print('Scanning Target '+Target)
print('Time Started ' + str(datetime.now()))
print('|' * 30)

try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(2)
            result = s.connect_ex((Target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
except KeyboardInterrupt:
   print('\nExiting PortScanner.py')
   sys.exit()
except socket.gaierror:
   print('Hostname could not be resolved')
   sys.exit()
except socket.error:
   print('Could not connect to server')
