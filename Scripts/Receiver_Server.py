import socket
from PIL import Image
import pickle

def server():
  host = socket.gethostname()   # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()
  s.bind((host, port))
  
  s.listen(1)
  client_socket, adress = s.accept()
  print("Connection from: " + str(adress))
  while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
      break
    print('From online user: ' + data)
    data = data.upper()
    client_socket.send(data.encode('utf-8'))
    print (data)
  client_socket.close()

def DisplayImage(image):
  #read the image
  #im = Image.open("D:/Documents/GitHub/noTABene/Scripts/test_img.png")
  #show image
  image.show()

def UnPackData(data):
  return pickle.dumps(data)

def PackData(data):
  return pickle.loads(data)

if __name__ == '__main__':
  DisplayImage()