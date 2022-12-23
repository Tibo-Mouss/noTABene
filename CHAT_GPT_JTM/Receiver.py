import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# bind to the port
s.bind((host, port))                                  

# queue up to 5 requests
s.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = s.accept()      

    print("Got a connection from %s" % str(addr))
    
    # receive image data and save it to a file
    with open('received_image.jpg', 'wb') as f:
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            # write data to a file
            f.write(data)
    
    # close the connection
    clientsocket.close()
