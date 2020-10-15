from configparser import ConfigParser
import configparser
import os
import sys
import subprocess
import socket

#EN ESTE SCRIPT SOLO SE AÑADIRAN FUNCCIONES PARA OBTENER INFORMACION DEL SYSTEMA

def ip_publica():
    get_ip = subprocess.call("curl ifconfig.me", shell=True)
    str_get_ip = str(get_ip)
    return str_get_ip

if __name__ == "__main__":
    #CREACION DE FICHER .INI
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config = ConfigParser()
    file = open(os.path.join(path, 'DATA/DATA.ini'), "w")

    config.add_section('system_info')
    config.set('system_info', 'IP_PUB', '2')
    
    config.write(file)

    file.close