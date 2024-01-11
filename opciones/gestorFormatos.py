import os
import archivo.modJson as mj
menu = ["Crear formato","Listar formato","Ir a menu principal"]

def formatos():
    formatos = {}
    isActiveFormatos = True
    while isActiveFormatos:
        os.system("cls")
        print("GESTOR DE FORMATOS")
        for i, indice in enumerate(menu):
            print(f"{i+1}. {indice}")
        try:
            opMenuFormatos = int(input("->"))
        except ValueError:
            print("El valo ingresado no es valido, intentelo de nuevo")
            os.system("pause")
        else:
            if (opMenuFormatos == 1):
                formato = {
                    'id': '',
                    'nombre': ''
                }
                os.system("cls")
                print("CREACION DE FORMATO")
                for indice in formato:
                    correctFormato = False
                    while (not correctFormato):
                        formato[indice] = input(f"Ingrese el {indice} del formato: ")
                        if (formato[indice] == ''):
                            print(f"Para continuar, debe ingresar el {indice} del formato.")
                            os.system("pause")
                        else:
                            correctFormato = True
                formatos.update({formato["id"]:formato})
                mj.crearArchivo(formatos,mj.ruta4)        
            elif (opMenuFormatos == 2):
                dataFormatos = mj.leerArchivo(mj.ruta4)
                for dict in dataFormatos.values():
                    print(f"{dict['id']}: {dict['nombre']}")
                os.system("pause")
            elif (opMenuFormatos == 3):
                isActiveFormatos = False
            else:
                print("El valo ingresado no es valido, intentelo de nuevo")
                os.system("pause")