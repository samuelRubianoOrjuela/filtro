import os
import archivo.modJson as mj
menu = ["Crear actor","Listar actores","Ir a menu principal"]

def actores():
    actores = {}
    isActiveActores = True
    while isActiveActores:
        os.system("cls")
        print("GESTOR DE ACTORES")
        for i, indice in enumerate(menu):
            print(f"{i+1}. {indice}")
        try:
            opMenuActores = int(input("->"))
        except ValueError:
            print("El valo ingresado no es valido, intentelo de nuevo")
            os.system("pause")
        else:
            if (opMenuActores == 1):
                actor = {
                    'id': '',
                    'nombre': ''
                }
                os.system("cls")
                print("CREACION DE ACTOR")
                for indice in actor:
                    correctActor = False
                    while (not correctActor):
                        actor[indice] = input(f"Ingrese el {indice} del actor: ")
                        if (actor[indice] == ''):
                            print(f"Para continuar, debe ingresar el {indice} del actor.")
                            os.system("pause")
                        else:
                            correctActor = True
                actores.update({actor["id"]:actor})
                mj.crearArchivo(actores,mj.ruta3)        
            elif (opMenuActores == 2):
                dataActores = mj.leerArchivo(mj.ruta3)
                for dict in dataActores.values():
                    print(f"{dict['id']}: {dict['nombre']}")
                os.system("pause")
            elif (opMenuActores == 3):
                isActiveActores = False
            else:
                print("El valo ingresado no es valido, intentelo de nuevo")
                os.system("pause")