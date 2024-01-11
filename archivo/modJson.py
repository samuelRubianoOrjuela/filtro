import os
import json

ruta1 = "data/peliculas.json"
ruta2 = "data/generos.json"
ruta3 = "data/actores.json"
ruta4 = "data/formados.json"

def crearArchivo(dict, ruta):
    with open(ruta,"w") as archvo:
        json.dump(dict,archvo,indent=4)

def leerArchivo(ruta):
    if os.path.exists(ruta):
        with open(ruta,"r") as archivo:
            data = json.load(archivo)
            return data
    else:
        print("gg")
        os.system("pause")

def actualizarArchivo(data, ruta):
    with open(ruta,"w") as archivo:
        json.dump(data,archivo,indent=4)