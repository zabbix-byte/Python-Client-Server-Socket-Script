# --*-- conding : utf8 --*-- 
from configparser import ConfigParser
import socket
import threading
import logging

#hadler
def handle_client(conn, addr):
    print(f"[NUEVA CONEXION] {addr} .")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")

    conn.close()

#iniciador de conecxion con los clientes
def start():
    server.listen()
    print("[ESCUCHANDO A CLIENTES]")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[CONEXIONES ACTIVAS] {threading.activeCount() -1}")



if __name__ == "__main__":
    #CONFIG FILE
    file = 'config_server.ini'
    config = ConfigParser()
    config.read(file)

    print("""
    
    [ENCENDIENDO..]
    By ZABBIX
    
    """)

    #parametros
    HEADER = config['CONFIG']['HEADER']
    PORT = config['CONFIG']['PORT']
    SERVER = config['CONFIG']['SERVER']
    ADDR = (SERVER, PORT)
    FORMAT = config['CONFIG']['FORMAT']

    #COMANDS
    DISCONNECT_MESSAGE = config['COMMANDS']['DISCONNECT_MESSAGE']
    

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    start()