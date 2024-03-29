import socket
import struct
import random

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT)) 
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
sock.settimeout(3)

id = random.randint(0, 10)
print(str(id))

while True:
    # data, addr = sock.recvfrom(1024)
    # Réception des données en provenance de la Raspberry Pi (ici, une image ou une vidéo)
    data = b''
    try:
        packet = sock.recv(4096)
    except:
        print("No message received")
    else:
        data+= packet
        with open("Images\ImageReceivedMulticast" + str(id) + ".png","wb") as f:
            f.write(data)
        print("Received Image Lets gooo")