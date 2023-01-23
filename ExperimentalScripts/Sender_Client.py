import socket
from utility import *

def client():
  host = "192.168.1.145"  # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()
  s.connect((host, port))

  img = Image.open("D:/Documents/GitHub/noTABene/Scripts/test_img.png")
  
  message = input('-> ')
  while message != 'q':
    s.send(PackData(img))
    data = s.recv(1024).decode('utf-8')
    print('Received from server: ' + data)
    message = input('==> ')
  s.close()

if __name__ == '__main__':
  img = Image.open("D:/Documents/GitHub/noTABene/Scripts/test_img.png")
  asyncio.run(tcp_echo_client(img))