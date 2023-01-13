import socket

# Créer un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecter le socket à l'adresse IP et au numéro de port de la Raspberry Pi
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # # Envoyer des données vers la Raspberry Pi (ici, une image ou une vidéo)
    # image_file = open("image.jpg", "rb")
    # image_data = image_file.read()
    # sock.sendall(image_data)

    # Réception des données en provenance de la Raspberry Pi (ici, une image ou une vidéo)
    data = b''
    while True:
        packet = sock.recv(4096)
        if not packet:
            break
        data+= packet

    print('received {!r}'.format(data))
    with open("received_image.png", "wb") as f:
        f.write(data)

finally:
    print('closing socket')
    sock.close()