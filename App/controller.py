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
 """

import config as cf
import model
import csv
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import shellsort
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(list_type):
    catalog = model.newCatalog(list_type)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadArtist(catalog)
    mergesort.sort(catalog["Artist"],comparar_artistas_creciente)
    loadArtworks(catalog)


def loadArtist(catalog):

    Artistfile = cf.data_dir + 'Artists-utf8-10pct.csv'
    input_file = csv.DictReader(open(Artistfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)


def loadArtworks(catalog):
    Artworks = cf.data_dir + 'Artworks-utf8-10pct.csv'
    input_file = csv.DictReader(open(Artworks, encoding='utf-8'))
    for Artwork in input_file:
        model.addArtwork(catalog, Artwork)

# Funciones de ordenamiento

def comparar_artistas_creciente(artista1,artista2):
    if artista1["Const.id"]<artista2["Const.id"]:
        return True
    else:
        return False

def comparar_artistas_cronologico_creciente(artista1,artista2):
    if artista1["Nacimiento"]<artista2["Nacimiento"]:
        return True
    else:
        return False

# Funciones de consulta sobre el catálogo
def artistas_cronologico(anio_i,anio_f,datos):
    datos = datos["Artist"].copy()
    shellsort.sort(datos,comparar_artistas_cronologico_creciente)
    inicio = model.binary_search(datos["elements"],0,lt.size(datos),"Nacimiento",anio_i)

    i = inicio
    lista = lt.newList('ARRAY_LIST')

    while datos["elements"][i]["Nacimiento"]<=anio_f and datos["elements"][i]["Nacimiento"] <= lt.lastElement(datos)["Nacimiento"]:
        lt.addLast(lista,datos["elements"][i])

        i += 1

    return lista

