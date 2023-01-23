import socket
from apscheduler.schedulers.background import BlockingScheduler

def Send_Image():
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    image_file = open("Images\ImageToSend.png", "rb")
    image_data = image_file.read()
    sock.sendto(image_data, (MCAST_GRP, MCAST_PORT))

    print("Image sent !")


def Say_Hello():
    print("hi")
    
sched = BlockingScheduler()
sched.add_job(Send_Image, 'interval', seconds =5)

sched.start()