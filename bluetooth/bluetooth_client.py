import socket

def create_connection(mac='B8:27:EB:54:43:36'):
    port = 3
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((mac, port))
    return s  

def send_wifi_credentials(username, password):
    s = create_connection()
    s.send(bytes(username, 'UTF-8'))
    s.send(bytes(password, 'UTF-8'))
    s.close()

if __name__ == "__main__":
    send_wifi_credentials("username", "password")