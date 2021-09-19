﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from datetime import datetime

import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def initCatalog(list_type):
    """
    Inicializa el catalogo
    """
    return controller.initCatalog(list_type)

def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    controller.loadData(catalog)


def printArtistasCronologicos(lista):
    mensaje1 = "El número de aritistas en este rango es: " + str(lt.size(lista))
    print(mensaje1)

    for i in range(1,4):
        incluir = []
        artista = lt.getElement(lista,i)
        incluir = [artista["Nombre"],artista["Nacimiento"],artista["Muerte"],artista["Nacionalidad"],artista["Genero"]]

        print(incluir)

    for i in range(lt.size(lista)-3, lt.size(lista)):
        incluir = []
        artista = lt.getElement(lista,i)
        incluir = [artista["Nombre"],artista["Nacimiento"],artista["Muerte"],artista["Nacionalidad"],artista["Genero"]]

        print(incluir)

def printAdquisicionesCronologicas(lista,compras):

    mensaje = "El número de obras adquiridas en este rango es: " + str(lt.size(lista))
    mensaje2 = "De las cuales " + str(compras) + " fueron compradas"
    print(mensaje)
    print(mensaje2)

    for i in range(1,4):
        incluir = []
        artwork = lt.getElement(lista,i)
        artistas_list = ""
        for artista in lt.iterator(artwork["Artistas"]):
            artistas_list += artista["Nombre"]


        incluir = [artwork["Titulo"],artistas_list,artwork["Fecha"],artwork["Medio"],artwork["Dimensiones"],"Fecha adquirida "+ str(artwork["Fecha_ad"])]

        print(incluir)
 

    for i in range(lt.size(lista)-3, lt.size(lista)):
        incluir = []
        artwork = lt.getElement(lista,i)
        artistas_list = ""
        for artista in lt.iterator(artwork["Artistas"]):
            artistas_list += artista["Nombre"]


        incluir = [artwork["Titulo"],artistas_list,artwork["Fecha"],artwork["Medio"],artwork["Dimensiones"],"Fecha adquirida "+ str(artwork["Fecha_ad"])]

        print(incluir)

def printObrasArtistaTecnica(nombre):
    pass

def printObrasNacionalidad(lista):
    print("Las nacionalidades con más obras son: ")
    for nacionalidad in lt.iterator(lista):
        mensaje = nacionalidad["Pais"] + ": " + str(nacionalidad["Count"])
        print(mensaje)
    
    print("--"*30)
    print("Para la nacionaliad más común, las siguientes son las 3 primeras y últimas obras de la lista: ")

    mayor_nacionalidad = lt.getElement(lista,1)
    for i in range(1,4):
        obra = lt.getElement(mayor_nacionalidad["Lista"],i)
        artistas_list = ""
        for artista in lt.iterator(obra["Artistas"]):
            artistas_list += artista["Nombre"]
        mensaje = [obra["Titulo"],artistas_list,obra["Fecha"],obra["Medio"],obra["Dimensiones"]]
        print(mensaje)

    for i in range(lt.size(lista)-3,lt.size(lista)):
        obra = lt.getElement(mayor_nacionalidad["Lista"],i)
        artistas_list = ""
        for artista in lt.iterator(obra["Artistas"]):
            artistas_list += artista["Nombre"]
        mensaje = [obra["Titulo"],artistas_list,obra["Fecha"],obra["Medio"],obra["Dimensiones"]]
        print(mensaje)

    

def printTrasportarObras(departamento):
    pass

def printNuevaProposicion(anio_i,anio_f,area_disponible):
    pass

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Listar cronológicamente los artistas")
    print("2- Listar cronológicamente las adquisiciones")
    print("3-Clasificar las obras de un artista por técnica")
    print("4-Clasificar las obras por la nacionalidad de sus creadores")
    print("5-Transportar obras de un departamento")
    print("6-Proponer una nueva exposición en el museo")
    print("7-Salir")

catalog = None
list_type = "ARRAY_LIST"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        catalog = initCatalog(list_type)
        loadData(catalog)
        print("Se cargaron exitosamente los datos")
        print("Aritistas cargados: "+ str(lt.size(catalog["Artist"])))
        print("Obras cargadas: "+ str(lt.size(catalog["Artwork"])))

    elif int(inputs[0]) == 1:
        anio_i = int(input("Ingrese el año de inicio: "))
        anio_f = int(input("Ingrese el año final: "))
        print("Cargando información de los archivos...")
        lista = controller.artistas_cronologico(anio_i,anio_f,catalog["Artist"])
        printArtistasCronologicos(lista)

    elif int(inputs[0]) == 2:
        fecha_i = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
        fecha_i = fecha_i.strip()
        fecha_i = datetime.strptime(fecha_i,"%Y-%m-%d")
        fecha_f = input("Ingrese la fecha final (YYYY-MM-DD): ")
        fecha_f = fecha_f.strip()
        fecha_f = datetime.strptime(fecha_f,"%Y-%m-%d")
        print("Cargando información de los archivos...")

        resultado = controller.adquisiciones_cronologico(fecha_i,fecha_f,catalog["Artwork"])
        printAdquisicionesCronologicas(resultado[0],resultado[1])

    elif int(inputs[0]) == 3:
        nombre_artista = input("Ingrese el nombre del artista: ")
        lista = controller.artistas_tecnica(nombre_artista)
        printObrasArtistaTecnica(nombre_artista)

    elif int(inputs[0]) == 4:
        print("Cargando información de los archivos...")
        resultado = controller.obras_nacionalidad(catalog["Artwork"])
        printObrasNacionalidad(resultado)

    elif int(inputs[0]) == 5:
        departamento = input("Ingrese el Departamento del museo del cual se transportan las obras: ")
        lista = controller.transporte_obras(departamento)
        printTrasportarObras(departamento)

    elif int(inputs[0]) == 6:
        anio_i = input("Ingrese el año inicial de las obras: ")
        anio_f = input("Ingrese el año final de las obras: ")
        area_disponible = input("Ingrese cuanta area (m^2) esta disponible para los objetos planos (cudros y fotos): ")
        anio_inicial = controller.proposicion_exposicion(catalog, anio_i)
        anio_final = controller.proposicion_exposicion(catalog, anio_f)
        area = controller.proposicion_exposicion(catalog, area_disponible)
        printNuevaProposicion(anio_i,anio_f,area_disponible)
    
    elif int(inputs[0])==7:
        break

    else:
        sys.exit(0)
sys.exit(0)
