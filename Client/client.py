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
    #Aqui se gritaran los recopiladores de datos 
    subprocess.call("py clientsysteminfo.py", shell=False)

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
 
    config.read(os.path.join(path, 'DATA/DATA.ini'))
    send(f"""
                                zabbix
     ✈ INFORMACION DEL SISTEMA CONECTADO : 

            Sistema operativo :  {str(config['system_info']['os_info'])}
            IP publica        :  {str(config['system_info']['IP_PUB'])}
            Puertos abiertos  :
            Usuarios sistema  :
            Ubificacion       :

     """)

    send(DISCONNECT_MESSAGE)

