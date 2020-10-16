import socket

hostMACAddress = 'B8:27:EB:54:43:36'
port = 3
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
print("Opened socket")
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print("Recieved ", data)
            client.send(data)
except: 
    print("Closing socket")     
    client.close()
    s.close()


