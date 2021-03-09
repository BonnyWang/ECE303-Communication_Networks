import sys 
import socket 

   
   
# Solve the input from the user
if len(sys.argv) > 2:
    if sys.argv[2] =='-p':
        portRange = sys.argv[3].split(":")

        if len(portRange) == 1:
            portRange.append(portRange[0])

        #Type conversion
        portRange[0] = int(portRange[0])
        portRange[1] = int(portRange[1])
    else:
        print("WARN: Invalid Input!")
else:
    
    # No port specified 
    portRange = [1,1024]

if len(sys.argv) < 2:
    print("WARN: Please enter the hostname")
    sys.exit()

host = socket.gethostbyname(sys.argv[1])  


for port in range(portRange[0], portRange[1]+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((host,port))
    if result == 0:
        print("Port " + str(port) +" is open" + " with service " + socket.getservbyport(port))


s.close()