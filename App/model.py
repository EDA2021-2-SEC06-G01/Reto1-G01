﻿"""
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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    
    catalog = {'Artist': None,
               'Artwork': None,}

    catalog['Artist'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compare)
    catalog['Artwork'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compare)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    artista = {}
    artista["Const.id"] = artist["ConstituentID"]
    artista["Nombre"] = artist["DisplayName"]
    artista["Nacionalidad"] = artist["Nationality"]
    artista["Nacimiento"] = artist["BeginDate"]
    artista["Muerte"] = artist["EndDate"]

    lt.addLast(catalog["Artist"],artista)    

def addArtwork(catalog,artwork):
    lt.addLast(catalog["Artwork"],artwork)




# Funciones para creacion de datos

def newArtist():

    Artist = {}
    return Artist


def newArtwork():

    Artwork = {}
    return Artwork


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(artistid,artist):
    if (artistid in artist['id']):
        return 0
    return -1


# Funciones de ordenamiento