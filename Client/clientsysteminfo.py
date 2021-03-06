from configparser import ConfigParser
import platform
import configparser
import os
import os.path
import sys
import subprocess
import socket


#EN ESTE SCRIPT SOLO SE AÑADIRAN FUNCCIONES PARA OBTENER INFORMACION DEL SYSTEMA

##OBTENEMOS EL USUARIO APARTIR DEL DIR 
def users_info():
    homedir = os.path.expanduser("~")
    homedir_lean = len(homedir)
    for i in reversed(range(homedir_lean)):
        if homedir[i] == "\\" or homedir[i] == "/":
            return homedir[i + 1 : -1 ] + homedir[-1]
    return "error"


##OBTENER SISTEMA OPERATIVO DEL CLIENTE
def os_info():
    os_info = platform.system() + " " + platform.release() + " " + os.name
    return str(os_info)


##OBTENER IP PUBLICA DEL CLIENTE
def ip_publica():
    get_ip = subprocess.check_output("curl http://ip.42.pl/raw", shell=True)
    str_get_ip = str(get_ip)
    cont_get_ip = str_get_ip[2:15]
    return cont_get_ip

if __name__ == "__main__":
    #CREACION DE FICHER .INI
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config = ConfigParser()
    file = open(os.path.join(path, 'DATA/DATA.ini'), "w")

    config.add_section('system_info')
    config.set('system_info', 'IP_PUB', ip_publica())
    config.set('system_info', 'os_info', os_info())
    config.set('system_info', 'os_user', users_info())
    config.write(file)

    file.close