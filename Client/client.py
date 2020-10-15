from configparser import ConfigParser
import socket
import subprocess
import threading
import logging
import os


#send funcciton
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



if __name__ == "__main__":
    #Config File
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config = ConfigParser()
    config.read(os.path.join(path, 'config_client.ini'))

    #parametres
    HEADER = int(config['CONFIG']['HEADER'])
    PORT = int(config['CONFIG']['PORT'])
    SERVER = str(config['CONFIG']['SERVER'])
    FORMAT = str(config['CONFIG']['FORMAT'])
    DISCONNECT_MESSAGE = "!DISCONNECT"
    ADDR = (SERVER, PORT)

    #connect 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    send("info_1")
    send("info_2")
    send("info_3")
    send(DISCONNECT_MESSAGE)

