import os
import archivo.modJson as mj
menu = ["Crear genero","Listar generos","Ir a menu principal"]

def generos():
    generos = {}
    isActiveGeneros = True
    while (isActiveGeneros):
        os.system("cls")
        print("GESTOR DE GENEROS")
        for i, dict in enumerate(menu):
            print(f"{i+1}. {dict}")
        try:
            opMenuGeneros = int(input("->"))
        except ValueError:
            print("El valo ingresado no es valido, intentelo de nuevo")
            os.system("pause")
        else:
            if (opMenuGeneros == 1):
                genero = {
                    'id': '',
                    'nombre': ''
                }
                os.system("cls")
                print("CREACION DE GENERO")
                for dict in genero:
                    correctGenero = False
                    while (not correctGenero):
                        genero[dict] = input(f"Ingrese el {dict} del genero: ")
                        if (genero[dict] == ''):
                            print(f"Para continuar, debe ingresar el {dict} del genero.")
                            os.system("pause")
                        else:
                            correctGenero = True
                generos.update({genero["id"]:genero})
                mj.crearArchivo(generos,mj.ruta2)        
            elif (opMenuGeneros == 2):
                dataGeneros = mj.leerArchivo(mj.ruta2)
                for dict in dataGeneros.values():
                    print(f"{dict['id']}: {dict['nombre']}")
                os.system("pause")
            elif (opMenuGeneros == 3):
                isActiveGeneros = False
            else:
                print("El valo ingresado no es valido, intentelo de nuevo")
                os.system("pause")