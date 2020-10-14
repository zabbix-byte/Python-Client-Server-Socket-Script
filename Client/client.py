from configparser import ConfigParser
import socket
import subprocess
import threading
import logging

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
    #Config File
    file = 'config_client.ini'
    config = ConfigParser()
    config.read(file)

    #parametres
    HEADER = config['CONFIG']['HEADER']
    PORT = config['CONFIG']['PORT']
    SERVER = config['CONFIG']['SERVER']
    FORMAT = config['CONFIG']['FORMAT']
    DISCONNECT_MESSAGE = "!DISCONNECT"
    ADDR = (SERVER, PORT)

    #connect 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    sends()


