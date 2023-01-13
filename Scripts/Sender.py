import socket
from PIL import Image

# Créer un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à une adresse IP et un numéro de port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Écouter les connexions entrantes
sock.listen(1)

while True:
    # Attendre une connexion
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # # Réception des données en provenance de l'ordinateur (ici, une image ou une vidéo)
        # data = connection.recv(16)
        # print('received {!r}'.format(data))

        # Envoi des données vers l'ordinateur (ici, une image ou une vidéo)
        image_file = open("Images\ImageToSend.png", "rb")
        # im = Image.open(r"Images\ImageToSend.png")
        # im.show()


        image_data = image_file.read()
        connection.sendall(image_data)
    finally:
        # Fermer la connexion
        connection.close()