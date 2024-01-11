import os

def edicion(peliculas):
    isActiveEdicion = True
    while (isActiveEdicion):
        os.system("cls")
        print("EDICION DE PELICULAS")
        print("Escoja la pelicula que desea editar.")
        for i, pelicula in enumerate(peliculas):
            print(f"{i+1},{pelicula}")
        print(f"{i+2}. Ir a gestor de peliculas")
        try:
            opMenuEd = int(input("->"))
        except ValueError:
            print("El valor de ingreso no es valido, intentelo de nuevo.")
            os.system("pause")
        else:
            for i, pelicula in enumerate(peliculas):
                if (i+1 == opMenuEd):
                    os.system("cls")
                    print(f"{pelicula["nombre"].capitalize()}:")
                elif (i+2 == opMenuEd):
                    isActiveEdicion = False

