import socket
from utility import *

def server():
  host = socket.gethostname()   # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()
  s.bind((host, port))

  data_received = []
  
  s.listen(1)
  client_socket, adress = s.accept()
  print("Connection from: " + str(adress))
  while True:
    data = client_socket.recv(1024)
    if not data:
      break
    print('From online user: ')
    #DisplayImage(UnPackData(data))
    data_received.append(data)
  client_socket.close()
  print("Server ended execution")
  image_unpacked = UnPackData(b"".join(data_received))
  DisplayImage(image_unpacked)


if __name__ == '__main__':
  asyncio.run(main())