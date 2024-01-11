import os
import opciones.gestorGeneros as gg
import opciones.gestorActores as ga
import opciones.gestorFormatos as gf
import opciones.gestorPeliculas as gp

if __name__ == '__main__':
    menu = ["Administrador de generos","Administrador de actores","Administrador de formatos","Gestor de informes","Gestor de peliculas","Salir"]
    isActive = True
    while (isActive):
        os.system("cls")
        print("SISTEMA GESTOR DE PELICULAS BLOCKBUSTER")
        for i, indice in enumerate(menu):
            print(f"{i+1}. {indice}")
        try:
            opMenu = int(input("->"))
        except ValueError:
            print("El valo ingresado no es valido, intentelo de nuevo")
            os.system("pause")
        else:
            if (opMenu == 1):
                gg.generos()
            elif (opMenu == 2):
                ga.actores()
            elif (opMenu == 3):
                gf.formatos()
            elif (opMenu == 4):
                pass
            elif (opMenu == 5):
                gp.peliculas()
            elif (opMenu == 6):
                isActive = False
            else:
                print("El valo ingresado no es valido, intentelo de nuevo")
                os.system("pause")