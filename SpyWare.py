import pyautogui
import getpass
import sys
import os
import random
import time

ruta = ""
usuario = ""

def tomarCapturas():
    print("Iniciando script\n")
    usuario = getpass.getuser()
    print("Nombre de usuario es " + usuario + "\n")

    if sys.platform.startswith("win32"):
        ruta = f"C:\\Users\\{usuario}\\Desktop\\"
        if not os.path.isdir(ruta + "CapturasSpyware"):
            print("Creando el directorio")
            os.mkdir(ruta + "CapturasSpyware")
            print("Directorio creado")
        ruta = ruta + "CapturasSpyware\\"

    elif sys.platform.startswith("linux"):
        print("Verificando ruta")
        ruta = f"/home/{usuario}/Pictures/"
        if not os.path.isdir(ruta + "CapturasSpyware"):
            print("Creando directorio de destino")
            os.mkdir(ruta + "CapturasSpyware")
        ruta = ruta + "CapturasSpyware/"

    file_name = "captura"

    while True:
        print("Realizando captura de pantalla...\n")
        random_time = random.randrange(2, 4)
        time.sleep(random_time)
        ts = time.time()
        ruta_final = f"{ruta}{file_name}_{ts}.jpg"
        captura = pyautogui.screenshot()
        captura.save(ruta_final)
        print("Captura de pantalla almacenada en: " + ruta_final + "\n")

tomarCapturas()