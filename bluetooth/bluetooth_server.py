import socket

data_format = "network={\
	ssid='{}'\
	psk='{}'\
	key_mgmt=WPA-PSK\
}"

all_data = []
num_messages = 0

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
            num_messages += 1
            all_data.append(data)
            print("Recieved ", data)
            client.send(data)
            if num_messages == 2:
                print(data_format.format(*all_data))
except: 
    print("Closing socket")     
    client.close()
    s.close()


