"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import getElement
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from datetime import datetime 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(list_type):
    
    catalog = {'Artist': None,
               'Artwork': None,}

    catalog['Artist'] = lt.newList(list_type,
                                    cmpfunction=compare)
    catalog['Artwork'] = lt.newList(list_type,
                                    cmpfunction=compare)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    artista = {}
    artista["Const.id"] = int(artist["ConstituentID"])
    artista["Nombre"] = artist["DisplayName"]
    artista["Nacionalidad"] = artist["Nationality"]
    artista["Nacimiento"] = int(artist["BeginDate"])
    artista["Muerte"] = artist["EndDate"]
    #artista["Obras"] = lt.newList("ARRAY_LIST",cmpfunction=compare)
    artista["Genero"] = artist["Gender"]

    lt.addLast(catalog["Artist"],artista)    

def addArtwork(catalog,artwork):
    obra = {}
    obra["id"]=artwork["ObjectID"]
    obra["Titulo"] = artwork["Title"]
    obra["Medio"] = artwork["Medium"]
    if artwork["DateAcquired"] != "":
        obra["Fecha_ad"] = datetime.strptime(artwork["DateAcquired"],"%Y-%m-%d")
    else:
        obra["Fecha_ad"] = datetime.strptime("0001-01-01","%Y-%m-%d")

    if artwork["Depth (cm)"] == "":
        obra["Profundidad"] = 0
    else:
        obra["Profundidad"] = artwork["Depth (cm)"]

    if artwork["Height (cm)"] == "":
        obra["Altura"] = 0
    else:
        obra["Altura"] = artwork["Height (cm)"]

    if artwork["Weight (kg)"] == "":
        obra["Peso"] = 0
    else:
        obra["Peso"] = artwork["Weight (kg)"]

    if artwork["Width (cm)"] == "":
        obra["Ancho"] = 0
    else:
        obra["Ancho"] = artwork["Width (cm)"]
    
    artistas = artwork["ConstituentID"]
    artistas = artistas.replace("[","")
    artistas = artistas.replace("]","")
    artistas = artistas.split(",")

    obra["Artistas"] = artistas

    if artwork["CreditLine"] == "Purchase":
        obra["Compra"] = True
    else:
        obra["Compra"]=False

   # for artista in artistas:
        #artista = int(artista)
        #posicion = None
        #posicion = binary_search(catalog["Artist"],0,lt.size(catalog["Artist"]),"Const.id",artista)
        #diccionario = lt.getElement(catalog["Artist"],posicion)["Obras"]
        #lt.addLast(diccionario,obra)

    lt.addLast(catalog["Artwork"],obra)




# Funciones para creacion de datos

def newArtist():

    Artist = {}
    return Artist


def newArtwork():

    Artwork = {}
    return Artwork


# Funciones de consulta

#def busqueda_artista_single(lista,artista):
    posicion = None
    for i in range(lt.size(lista)):
        if lt.getElement(lista,i)["Const.id"] == artista:
            posicion = i
            break
    return posicion

def binary_search(arr, low, high,key, x):
    #Tomado y modificado de https://www.geeksforgeeks.org/python-program-for-binary-search/
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if lt.getElement(arr,mid)[key] == x:
            #Revisar si hay duplicados
            while lt.getElement(arr,mid)[key] == lt.getElement(arr,mid-1)[key]:
                mid -= 1
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif lt.getElement(arr,mid)[key] > x:
            return binary_search(arr, low, mid - 1,key, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high,key, x)
 
    else:
        # Element is not present in the array
        return -1

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(artist1,artist):
    artist = artist["Const.id"]
    if artist1 == artist:
        return 0
    return -1


def comparedate(artwork1,artwork2):
    if artwork1["Fecha_ad"] < artwork2["Fecha_ad"]:
        return True
    else:
        return False

# Funciones de ordenamiento