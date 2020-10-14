import socket
import subprocess

#send funcciton
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def sends():
    send("")
    send("Ya estoy aqui")
    send(DISCONNECT_MESSAGE)


if __name__ == "__main__":
    #parametres
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "192.168.0.204"
    ADDR = (SERVER, PORT)

    #connect 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    sends()


