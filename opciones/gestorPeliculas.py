import os
import archivo.modJson as mj
import opPeliculas.edicionPeliculas as ep

menu = ["Agregar pelicula","Editar pelicula","Eliminar pelicula","Eliminar Actor","Buscar pelicula","Listar todas peliculas","Ir a menu principal"]

def itemDict(item, ruta, pelicula):
    dataDict = mj.leerArchivo(ruta)
    print(f"{item.capitalize()}")
    for i, dict in enumerate(dataDict.values()):
        print(f"{i+1}. {dict['id']}: {dict['nombre']}")
    correctInput = True
    while correctInput:
        try:
            opMenuDict = int(input("->"))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo")
            os.system("pause")
        else:
            cont = 0
            for i, dict in enumerate(dataDict.values()):
                if (i+1 == opMenuDict):
                    pelicula[item] = {dict['id']: dict}
                else:
                    cont += 1
            if (cont > i):
                print("El valor ingresado no es valido, intentelo de nuevo")
                os.system("pause")
            else:
                correctInput = False

def peliculas():   
    tiendaPeliculas = {
        'blockbuster':{
            'peliculas':{}
        }
    }  
    isActiveActores = True
    while isActiveActores:
        os.system("cls")
        print("GESTOR DE ACTORES")
        for i, item in enumerate(menu):
            print(f"{i+1}. {item}")
        try:
            opMenuPeliculas = int(input("->"))
        except ValueError:
            print("El valor ingresado no es valido, intentelo de nuevo")
            os.system("pause")
        else:
            if (opMenuPeliculas == 1):
                pelicula = {
                    'id': '',
                    'nombre': '',
                    'duracion': '',
                    'sinopsis': '',
                    'generos': {},
                    'actores': {},
                    'formato': {},
                    }
                os.system("cls")
                print("AGREGAR PELICULA")
                for item in pelicula:   
                    if (item == 'generos'):
                        itemDict(item, mj.ruta2, pelicula)
                    elif (item == 'actores'):
                        itemDict(item, mj.ruta3, pelicula)
                    elif (item == 'formato'):
                        itemDict(item, mj.ruta4, pelicula)
                    else:
                        correctPelicula = False
                        while (not correctPelicula):
                            pelicula[item] = input(f"Ingrese {item} de la pelicula: ")
                            if (pelicula[item] == ''):
                                print(f"Para continuar, debe ingresar el {item} de la pelicula.")
                                os.system("pause")
                            else:
                                correctPelicula = True
                tiendaPeliculas["blockbuster"]["peliculas"].update({pelicula["id"]:pelicula})
                mj.crearArchivo(tiendaPeliculas, mj.ruta1)
            elif (opMenuPeliculas == 2):
                ep.edicion(tiendaPeliculas["blockbuster"]["peliculas"])
            elif (opMenuPeliculas == 3):
                pass
            elif (opMenuPeliculas == 4):
                pass
            elif (opMenuPeliculas == 5):
                pass
            elif (opMenuPeliculas == 6):
                pass
            elif (opMenuPeliculas == 7):
                pass
            else:
                print("El valor ingresado no es valido, intentelo de nuevo")
                os.system("pause")
