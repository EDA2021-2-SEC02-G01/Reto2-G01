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


from DISClib.DataStructures.arraylist import subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as qu
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf
import time 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newGallery(type):
    gallery = {"artwork":None,"artists":None}
    gallery["artwork"] = lt.newList(type)
    gallery["artists"] = lt.newList(type)
    return gallery

def ArtistNationGallery():
    return {}


# Funciones para agregar informacion al catalogo
def addArtwork(gallery, artwork):
    lt.addLast(gallery["artwork"], artwork)
    

def addArtist(gallery, artist):
    lt.addLast(gallery["artists"], artist)


# Funciones para creacion de datos

"""def newArtist(artist_info):
    return artist_info"""
# Funciones de consulta
def requerimiento_1(gallery,ai,af):
    nueva = lt.newList("ARRAY_LIST")
    for i in range(lt.size(gallery["artists"])):
        actual = lt.getElement(gallery["artists"],i)
        if ai<=actual["BeginDate"]<=af:
            lt.addLast(nueva,actual)
    return nueva

def fecha_dias(fecha):
    data = fecha.split("-")
    if data[0] == "":
        suma = 0
    else:
        suma = 0
        suma = int(data[0])*360
        try:
            suma += int(data[1])*30
            suma += int(data[2])
        except:
            pass
    return suma

def requerimiento_2(gallery,fi,ff):
    lista = lt.newList("ARRAY_LIST")
    dias_1 = fecha_dias(fi)
    dias_2 = fecha_dias(ff)
    cont = 0
    for i in range(lt.size(gallery["artwork"])):
        actual = lt.getElement(gallery["artwork"],i)
        if dias_1 <= fecha_dias(actual["DateAcquired"]) <= dias_2:
            lt.addLast(lista,actual)
        if "purchase" in actual["CreditLine"].lower():
            cont += 1
    return lista,cont

def requerimiento_3(gallery, name, sorted_artists):
    pos = 0
    for i in range(lt.size(sorted_artists)):
        actual = lt.getElement(sorted_artists,i)
        if actual["DisplayName"].lower() == name.lower():
            pos = i
            break
    artist = lt.getElement(sorted_artists,pos)
    artist_id = artist["ConstituentID"]
    lista = lt.newList("ARRAY_LIST")
    for i in range(lt.size(gallery["artwork"])):
        actual = lt.getElement(gallery["artwork"],i)
        if artist_id in actual["ConstituentID"]:
            lt.addLast(lista,actual)
    return lista
def contar_tecnica(data):
    ret = {}
    for i in range(lt.size(data)):
        actual = lt.getElement(data,i)
        ret[actual["Medium"]] = ret.get(actual["Medium"],0) + 1
    max = 0
    style = ""
    for k,v in ret.items():
        if v > max:
            max = v
            style = k
    tecnica = lt.newList("ARRAY_ELEMENT")
    for i in range(lt.size(data)):
        actual = lt.getElement(data,i)
        if actual["Medium"] == style:
            lt.addLast(tecnica,actual)
    return tecnica

def obras_departamento(gallery, department):
    obras = lt.newList("ARRAY_LIST")
    for i in range(lt.size(gallery["artwork"])):
        actual = lt.getElement(gallery["artwork"],i)
        if actual["Department"].lower() == department.lower():
            lt.addLast(obras,actual)
    return obras

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    return artwork1["DateAcquired"] < artwork2["DateAcquired"]

def cmpNationsByArtists(nation1,nation2):
    return nation1[1] > nation2[1]

def cmpArtistByID(artist_1,artist_2):
    return artist_1["ConstituentID"] > artist_2["ConstituentID"]

def cmpArtistByName(artist_1,artist_2):
    return artist_1["DisplayName"] > artist_2["DisplayName"]
def cmpArtworkByAge(artwork_1,artwork_2):
    return artwork_1["Date"]>artwork_2["Date"]

def cmpArtworkByCost(costo_1,costo_2):
    return costo_1["cost"]>costo_2["cost"]


# Funciones de ordenamiento
def sortArtworks(gallery, size, sort_type):
    sublist = lt.subList(gallery["artwork"],1,size)
    ordenar = sublist.copy()
    init_time = time.process_time()
    if sort_type == "1":
        sorted = sa.sort(ordenar, cmpArtworkByDateAcquired)
    elif sort_type == "2":
        sorted = qu.sort(ordenar, cmpArtworkByDateAcquired)
    elif sort_type == "3":
        sorted = mg.sort(ordenar, cmpArtworkByDateAcquired)
    else:
        sorted = ins.sort(ordenar, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    time_mseg = (stop_time - init_time)*1000
    return time_mseg, sorted

def sortByArtistID(gallery):
    sublista = lt.subList(gallery["artists"],1,lt.size(gallery["artists"]))
    a_ordenar = sublista.copy()
    sorted = sa.sort(a_ordenar, cmpArtistByID)
    return sorted

def sortByArtistName(gallery):
    sublista = lt.subList(gallery["artists"],1,lt.size(gallery["artists"]))
    a_ordenar = sublista.copy()
    sorted = sa.sort(a_ordenar, cmpArtistByName)
    return sorted

def busqueda_binaria(low, high, artists_sorted, value):
    if high >= low:
        middle = int((high+low)/2)
        if lt.getElement(artists_sorted,middle)["ConstituentID"] == value:
            return middle
        elif lt.getElement(artists_sorted,middle)["ConstituentID"] > value:
            return busqueda_binaria(low, middle-1, artists_sorted, value)
        else:
            return busqueda_binaria(middle+1, high, artists_sorted, value)
    else:
        return -1

def busqueda_binaria_nombre_ID(low, high, artists_sorted, value):
    if high >= low:
        middle = int((high+low)/2)
        if lt.getElement(artists_sorted,middle)["DisplayName"].lower() == value.lower():
            return middle
        elif lt.getElement(artists_sorted,middle)["DisplayName"].lower() > value.lower():
            return busqueda_binaria(low, middle-1, artists_sorted, value.lower())
        else:
            return busqueda_binaria(middle+1, high, artists_sorted, value.lower())
    else:
        return -1


def sortArtist(gallery,artists,artwork,artist_sorted):
    art_artists = artwork["ConstituentID"]
    if not "," in art_artists:
        art_artists = art_artists[1:len(art_artists)-1]
        art_artists = [art_artists]
    else:
        art_artists = art_artists.split(",")
        art_artists[0] = art_artists[0][1:]
        art_artists[len(art_artists)-1] = art_artists[len(art_artists)-1][:len(art_artists[len(art_artists)-1])-2]
    for i in art_artists:
        for j in range(lt.size(gallery["artists"])):
            actual = lt.getElement(gallery["artists"],j)
            autores = actual["ConstituentID"]
            if autores == i:
                artist = actual
                break
        if artist["Nationality"] not in artists:
            artists[artist["Nationality"]] = lt.newList("ARRAYLIST")
        lt.addLast(artists[artist["Nationality"]],artwork)


def sortArtistsbyNation(sorted_artists):
    sorted = lt.newList("ARRAY_LIST")
    for i in sorted_artists:
        lt.addLast(sorted,(i,lt.size(sorted_artists[i])))
    return mg.sort(sorted,cmpNationsByArtists)


def añadir_costo(obra):
    valores = []
    try:
        dimensiones = obra["Dimensions"]
        dimensiones = dimensiones.split("x")
        dimensiones[0] = dimensiones[0].strip()[1:]
        dimensiones[1] = dimensiones[1].strip().replace("cm","")
        valores.append(float(dimensiones[0])*float(dimensiones[1])*72)
    except:
        pass
    try:
        peso = obra["Weight (kg)"]
        valores.append(float(peso)*72)
    except:
        pass
    try:
        dimensiones = [obra["Height (cm)"],obra["Length (cm)"],obra["Width (cm)"]]
        vol = 1
        for i in dimensiones:
            vol *= float(i)
        valores.append(vol * 72)
    except:
        pass
    if len(valores) == 0:
        valor = 46
    else:
        valor = max(valores)
    obra["cost"] = valor

def estimar_valor(obras):
    valor = 0
    for i in range(lt.size(obras)):
        actual = lt.getElement(obras,i)
        valores = []
        try:
            dimensiones = actual["Dimensions"]
            dimensiones = dimensiones.split("x")
            dimensiones[0] = dimensiones[0].strip()[1:]
            dimensiones[1] = dimensiones[1].strip().replace("cm","")
            valores.append(float(dimensiones[0])*float(dimensiones[1])*72)
        except:
            pass
        try:
            peso = actual["Weight (kg)"]
            valores.append(float(peso)*72)
        except:
            pass
        try:
            dimensiones = [actual["Height (cm)"],actual["Length (cm)"],actual["Width (cm)"]]
            vol = 1
            for i in dimensiones:
                vol *= float(i)
            valores.append(vol * 72)
        except:
            pass
        if len(valores) == 0:
            valor += 46
        else:
            valor += max(valores)
    return valor
        
def obras_antiguas(departamento):
    sublista = lt.subList(departamento,1,lt.size(departamento))
    a_ordenar = sublista.copy()
    sorted = sa.sort(a_ordenar, cmpArtworkByAge)
    return sorted

def obras_costosas(departamento):
    sublista = lt.subList(departamento,1,lt.size(departamento))
    a_ordenar = sublista.copy()
    for i in range(lt.size(a_ordenar)):
        actual = lt.getElement(a_ordenar,i)
        añadir_costo(actual)
    sorted = sa.sort(a_ordenar, cmpArtworkByCost)
    return sorted

