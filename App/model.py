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
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as qu
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf
import time 
from DISClib.DataStructures import mapentry as me


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newGallery(type):
    gallery = {"artwork":None,"artists":None,"Medium":None}
    gallery["artwork"] = lt.newList(type)
    gallery["artists"] = lt.newList(type)
    #MODIFICACION LAB 5
    gallery["Medium"] = mp.newMap(22000,maptype="CHAINING",loadfactor=4.0)
    gallery["ConstituentID"] = mp.newMap(15230,maptype="CHAINING",loadfactor=5.0)
    gallery["Nationality"] = mp.newMap(15230, maptype="CHAINING",loadfactor=4.0)
    gallery["BeginDate"] = mp.newMap(15230,maptype="CHAINING",loadfactor=4.0)
    gallery["DateAcquired"] = mp.newMap(15230,maptype="CHAINING",loadfactor=4.0)
    gallery["ArtworkID"] = mp.newMap(140000,maptype="CHAINING",loadfactor=4.0)
    gallery["Department"] = mp.newMap(15230,maptype="CHAINING",loadfactor=4.0)
    gallery["ArtistID"] = mp.newMap(15230,maptype="CHAINING",loadfactor=4.0)

    return gallery

def ArtistNationGallery():
    return {}


# Funciones para agregar informacion al catalogo
def addArtwork(gallery, artwork):
    lt.addLast(gallery["artwork"], artwork)
    #MODIFICACION LAB 5
    

def addMedium(gallery,artwork,medio):
    objeto = gallery["Medium"]
    exist_medium = mp.contains(objeto,medio)
    if exist_medium:
        entrada = mp.get(objeto,medio)
        ob = me.getValue(entrada)
    else:
        ob = lt.newList("ARRAY_LIST",cmpfunction=cmpArtworkByDateAcquired)
        mp.put(gallery["Medium"],medio,ob)
    lt.addLast(ob, artwork)

def addArtID(gallery,artwork,ids):
    mapa_interes = gallery["ArtworkID"]
    for i in ids:
        existe = mp.contains(mapa_interes,i)
        if not existe:
            ob = lt.newList("ARRAY_LIST")
            mp.put(mapa_interes,i,ob)
        else:
            entrada = mp.get(mapa_interes,i)
            ob = me.getValue(entrada)
        lt.addLast(ob,artwork)

def addArtistbyID(gallery,artwork,ids):
    objeto = gallery["ArtistID"]
    esta = mp.contains(objeto,ids)
    if not esta:
        mp.put(objeto,ids,artwork)

def addArtworkDepartment(gallery,artwork,department):
    mapa_interes = gallery["Department"]
    existe = mp.contains(mapa_interes, department)
    if existe:
        entrada = mp.get(mapa_interes,department)
        ob = me.getValue(entrada)
    else:
        ob = lt.newList("ARRAY_LIST")
        mp.put(mapa_interes,department,ob)
    lt.addLast(ob,artwork)

def requerimiento_5(gallery,department):
    ob = mp.get(gallery["Department"],department)
    return me.getValue(ob)

def obtener_id(gallery,nombre):
    for i in lt.iterator(mp.keySet(gallery["ArtistID"])):
        actual = mp.get(gallery["ArtistID"],i)
        artista = me.getValue(actual)
        if artista["DisplayName"].lower() == nombre.lower():
            return artista["ConstituentID"] 

def addArtist_CID(gallery, artist, constituentID):
    objeto = gallery["ConstituentID"]
    esta = mp.contains(objeto, constituentID)
    if esta == False:
        mp.put(objeto,constituentID,artist["Nationality"])



def addArtistBeginDate(gallery, artist, begin_date):
    objeto = gallery["BeginDate"]
    esta = mp.contains(objeto,begin_date)
    if esta:
        entrada = mp.get(objeto,begin_date)
        ob = me.getValue(entrada)
    else:
        ob = lt.newList("ARRAY_LIST")
        mp.put(gallery["BeginDate"],begin_date,ob)
    lt.addLast(ob,artist)


def addMedium_nationality(gallery,artwork,todos_ids):
    objeto = gallery["Nationality"]
    ids = gallery["ConstituentID"]
    for i in todos_ids:
        nacionalidad = mp.get(ids,i)
        if nacionalidad != None:
            nacionalidad = me.getValue(nacionalidad)
            exist_medium = mp.contains(objeto,nacionalidad)
            if exist_medium:
                entrada = mp.get(objeto,nacionalidad)
                ob = me.getValue(entrada)
            else:
                ob = lt.newList("ARRAY_LIST",cmpfunction=cmpArtworkByNationality)
                mp.put(gallery["Nationality"],nacionalidad,ob)
            lt.addLast(ob, artwork)

def addMediumDateacq(gallery,artwork,date):
    objeto = gallery["DateAcquired"]
    esta = mp.contains(objeto,date)
    if not esta:
        ob = lt.newList("ARRAY_LIST",cmpfunction=cmpArtworkByDateAcquired)
        mp.put(objeto,date,ob)
    else:
        entrada = mp.get(objeto,date)
        ob = me.getValue(entrada)
    lt.addLast(ob,artwork)

def addArtist(gallery, artist):
    lt.addLast(gallery["artists"], artist)


# Funciones para creacion de datos

"""def newArtist(artist_info):
    return artist_info"""
# Funciones de consulta
def requerimiento_1(gallery,ai,af):
    nueva = lt.newList("ARRAY_LIST")
    interes = gallery["BeginDate"]
    for i in range(int(ai),int(af)+1):
        objeto = mp.get(interes,str(i))
        artistas = me.getValue(objeto)
        for j in lt.iterator(artistas):
            lt.addLast(nueva,j)
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
    for i in lt.iterator(mp.keySet(gallery["DateAcquired"])):
        dias = fecha_dias(i)
        if dias_1 <= dias <= dias_2:
            obj = mp.get(gallery["DateAcquired"],i)
            for j in lt.iterator(me.getValue(obj)):
                lt.addLast(lista,j)
                if "purchase" in j["CreditLine"]:
                    cont += 1
    return lista,cont

def buscar_id(gallery,id):
    objeto = gallery["ConstituentID"]
    artista = mp.get(objeto,id)
    return me.getValue(artista)

def requerimiento_3(gallery, id):
    lista = mp.get(gallery["ArtworkID"],id)
    return lista

def contar_tecnica(data):
    ret = {}
    aux = lt.newList("ARRAY_ELEMENT")
    for i in range(lt.size(data)):
        actual = lt.getElement(data,i)
        ret[actual["Medium"]] = ret.get(actual["Medium"],0) + 1
    max = 0
    style = ""
    for k,v in ret.items():
        lt.addLast(aux,(k,v))
        if v > max:
            max = v
            style = k
    tecnica = lt.newList("ARRAY_ELEMENT")
    for i in range(lt.size(data)):
        actual = lt.getElement(data,i)
        if actual["Medium"] == style:
            lt.addLast(tecnica,actual)
    ordenada = mg.sort(aux,cmpList)
    return tecnica,ordenada

def obras_departamento(gallery, department):
    obras = lt.newList("ARRAY_LIST")
    for i in range(lt.size(gallery["artwork"])):
        actual = lt.getElement(gallery["artwork"],i)
        if actual["Department"].lower() == department.lower():
            lt.addLast(obras,actual)
    return obras



#MODIFICACION LAB 5
def ReqLab5(gallery, medium):
    medio = mp.get(gallery["Medium"], medium)
    if medio:
        return me.getValue(medio)
    return None

def requerimiento_4(obj):
    nueva = lt.newList("ARRAY_LIST")
    for i in lt.iterator(mp.keySet(obj)):
        actual = mp.get(obj,i)
        valor = lt.size(me.getValue(actual))
        temp = (i,valor)
        lt.addFirst(nueva,temp)
    nueva_sorted = mg.sort(nueva,cmpList)
    return nueva_sorted

def cmpList(nat1,nat2):
    return nat1[1]>nat2[1]
#LAB 6
def obtener_obras_nacionalidad(gallery, nacionalidad):
    obj = mp.get(gallery["Nationality"], nacionalidad)
    if obj:
        return me.getValue(obj)
    return None


def obtener_obras_nacionalidad_v2(gallery, nacionalidad):
    obj = mp.get(gallery["Nationality"], nacionalidad)
    if obj:
        return me.getValue(obj)
    return None
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

def cmpArtworkByNationality(artwork_1, artwork_2):
    return artwork_1["Nationality"] >artwork_2["Nationality"]

"""def compareMedium():
    pass"""


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

def n_obras(lista,n):
    sublista = lt.subList(lista,1,n)
    ret = sublista.copy()
    return ret

def bono(gallery,artistas):
    obras = lt.newList("ARRAY_LIST")
    interes = gallery["ArtworkID"]
    for i in lt.iterator(artistas):
        todas = mp.get(interes,i["ConstituentID"])
        lt.addLast(obras, (i["DisplayName"],lt.size(todas)))
        i["cantidad"] = lt.size(todas)
    ordenada = mg.sort(obras,cmpList)
    return ordenada

