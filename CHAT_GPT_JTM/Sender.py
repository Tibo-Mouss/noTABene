import socket
import time

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# open image file
with open('imageToSend.png', 'rb') as f:
    # send image file
    s.sendall(f.read())

# close the connection
s.close()
