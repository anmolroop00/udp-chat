import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.1.43",1234))
print("Server Started")
def receiver():
    while True:
        x = s.recvfrom(1024)
        y=x[1][0]
        x=x[0].decode()
        print("\t\t{0}:{1}".format(y,x))

def sender():
    while True:
        message = input()
        s.sendto(message.encode(), ("192.168.1.7", 1234))

x1 = threading.Thread(target = receiver)
x2 = threading.Thread(target = sender)
x1.start()
x2.start()

