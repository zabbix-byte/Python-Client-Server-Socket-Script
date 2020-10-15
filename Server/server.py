# --*-- conding : utf8 --*-- 
from configparser import ConfigParser
import os
import socket
import threading
import logging

#hadler
def handle_client(conn, addr):
    print(f"[Nueva Conexion] {addr} .")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Recivido".encode(FORMAT))
    
    
    conn.close()

#iniciador de conecxion con los clientes
def start():
    server.listen()
    print(f"[Escuchando] {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Conexiones activas] {threading.activeCount() - 1}")




if __name__ == "__main__":
    #CONFIG FILE
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config = ConfigParser()
    config.read(os.path.join(path, 'config_server.ini'))
    #parametros
    HEADER = int(config['CONFIG']['HEADER'])
    PORT = int(config['CONFIG']['PORT'])
    SERVER = str(config['CONFIG']['SERVER'])
    ADDR = (SERVER, PORT)
    FORMAT = str(config['CONFIG']['FORMAT'])

    #COMANDS
    DISCONNECT_MESSAGE = config['COMMANDS']['DISCONNECT_MESSAGE']

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    print("""
    
    [ENCENDIENDO..]
    By ZABBIX
    
    """)



    start()
