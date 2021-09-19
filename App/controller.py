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
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort
from DISClib.ADT import list as lt
import time


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
    shellsort.sort(catalog["Artist"],comparar_artistas_creciente)
    loadArtworks(catalog)


def loadArtist(catalog):

    Artistfile = cf.data_dir + 'Artists-utf8-large.csv'
    input_file = csv.DictReader(open(Artistfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)


def loadArtworks(catalog):
    Artworks = cf.data_dir + 'Artworks-utf8-large.csv'
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

#def sortbydate(list,sort_type):
    start_time = time.process_time()
    if sort_type == 1:
        insertionsort.sort(list,model.comparedate)
    elif sort_type == 2:
        shellsort.sort(list,model.comparedate)
    elif sort_type == 3:
        mergesort.sort(list,model.comparedate)
    else:
        quicksort.sort(list,model.comparedate)
    stop_time = time.process_time()
    dtime = (stop_time-start_time)*1000
    return list,dtime



# Funciones de consulta sobre el catálogo
def artistas_cronologico(anio_i,anio_f,datos):
    datos = datos.copy()
    shellsort.sort(datos,comparar_artistas_cronologico_creciente)
    inicio = model.binary_search(datos,0,lt.size(datos),"Nacimiento",anio_i)

    i = inicio
    lista = lt.newList('ARRAY_LIST')

    while lt.getElement(datos,i)["Nacimiento"]<=anio_f and lt.getElement(datos,i)["Nacimiento"] <= lt.lastElement(datos)["Nacimiento"]:
        lt.addLast(lista,lt.getElement(datos,i))
        i += 1

    return lista

def adquisiciones_cronologico(fecha_i,fecha_f,datos,):
    datos = datos.copy()
    shellsort.sort(datos,model.comparedate)

    inicio = model.binary_search(datos,0,lt.size(datos),"Fecha_ad",fecha_i)

    i = inicio
    lista = lt.newList("ARRAY_LIST")
    compras = 0

    while lt.getElement(datos,i)["Fecha_ad"] <= fecha_f and lt.getElement(datos,i)["Fecha_ad"] <= lt.lastElement(datos)["Fecha_ad"]:
        lt.addLast(lista,lt.getElement(datos,i))
        if lt.getElement(datos,i)["Compra"] == True:
            compras += 1
        i += 1

    return lista,compras

def obras_nacionalidad(datos):
    histograma = {}
    for obra in lt.iterator(datos):
        for artista in lt.iterator(obra["Artistas"]):
            nacionalidad = artista["Nacionalidad"]
            if nacionalidad in histograma:
                histograma[nacionalidad]["Count"] += 1
                lt.addLast(histograma[nacionalidad]["Lista"],obra)
            elif nacionalidad != "":
                histograma[nacionalidad] = {}
                histograma[nacionalidad]["Pais"] = nacionalidad
                histograma[nacionalidad]["Count"] = 1
                histograma[nacionalidad]["Lista"] = lt.newList("ARRAY_LIST")
                lt.addLast(histograma[nacionalidad]["Lista"],obra)
            else:
                continue
    
    orden = lt.newList("ARRAY_LIST")
    for i in range(0,10):
        numero_mayor = 0
        pais_mayor = ""
        for pais in histograma:
            if histograma[pais]["Count"]>numero_mayor:
                numero_mayor = histograma[pais]["Count"]
                pais_mayor = histograma[pais]["Pais"]
            else:
                continue
        
        lt.addLast(orden,histograma[pais_mayor].copy())
        histograma[pais_mayor]["Count"] = -1
    return orden

def transporte_obras(departamento,datos):
    datos = datos.copy()
    shellsort.sort(datos,model.compare_department)
    inicio = model.binary_search(datos,0,lt.size(datos),"Departamento",departamento)
    i = inicio
    lista = lt.newList("ARRAY_LIST")
    precio_acumulado = 0
    peso_acumulado = 0
    mas_costosas = lt.newList("ARRAY_LIST")

    for k in range(0,5):
        obra_dummy = {"Obra":None,"Precio":0}
        lt.addLast(mas_costosas,obra_dummy)


    while lt.getElement(datos,i)["Departamento"] == departamento:
        elemento = lt.getElement(datos,i)
        obra = {}
        obra["Obra"] = elemento

        P_area = elemento["Altura"]*elemento["Ancho"]*72
        P_vol = elemento["Altura"]*elemento["Ancho"]*elemento["Profundidad"]*72
        P_peso = elemento["Peso"]*72
        precio = max(P_area,P_vol,P_peso)

        if precio == 0:
            precio = 48
        
        obra["Precio"] = round(precio,2)
        lt.addLast(lista,obra)
        precio_acumulado += precio
        peso_acumulado += elemento["Peso"]

        pos_min = None
        precio_min = 1000*100000
        for j in range(1,lt.size(mas_costosas)+1):
            valor = lt.getElement(mas_costosas,j)["Precio"]
            if valor < precio_min:
                precio_min = valor
                pos_min = j
        
        if precio > precio_min:
            lt.changeInfo(mas_costosas,pos_min,obra)

        i += 1
    
    insertionsort.sort(mas_costosas,model.compare_price)


    return lista,precio_acumulado,peso_acumulado,mas_costosas

#def create_sublist(list,size):
    #if size < lt.size(list):
        
        #lista = lt.subList(list,0,size)
        #return lista
    
    #else:
        #return -1


