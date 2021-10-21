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
from DISClib.ADT import list as lt
import time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras
def initGallery(type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    gallery = model.newGallery(type)
    return gallery

def initArtists():
    return model.ArtistNationGallery()

# Funciones para la carga de datos

def loadData(gallery):
    """
    Carga los datos de los archivos 
    """
    start = time.process_time()
    loadArtists(gallery)
    loadArtworks(gallery)
    stop = time.process_time()
    elapsed_time_mseg = (stop - start)*1000
    print(f"El tiempo de carga fue de {elapsed_time_mseg} mseg")

def loadArtists(gallery):
    """
    Carga los artistas de un archivo. 
    """
    artistFile = cf.data_dir + "MoMA/Artists-utf8-large.csv"
    input_file = csv.DictReader(open(artistFile, encoding="utf-8"))
    for artist in input_file:
        model.addArtist(gallery, artist)
        model.addArtist_CID(gallery,artist,artist["ConstituentID"])
        model.addArtistBeginDate(gallery,artist,artist["BeginDate"])
        model.addArtistbyID(gallery,artist,artist["ConstituentID"])

def loadArtworks(gallery):
    """
    Carga los artworks de un archivo
    """
    artworksFile = cf.data_dir + "MoMA/Artworks-utf8-large.csv"
    input_file = csv.DictReader(open(artworksFile,encoding="utf-8"))
    for artwork in input_file:
        model.addArtwork(gallery, artwork)
        model.addMedium(gallery,artwork,artwork["Medium"])
        model.addMediumDateacq(gallery,artwork,artwork["DateAcquired"])
        model.addArtworkDepartment(gallery,artwork,artwork["Department"])
        art_artists = artwork["ConstituentID"]
        if not "," in art_artists:
            art_artists = art_artists[1:len(art_artists)-1]
            art_artists = [art_artists]
        else:
            art_artists = art_artists.split(",")
            art_artists[0] = art_artists[0][1:]
            art_artists[len(art_artists)-1] = art_artists[len(art_artists)-1][:len(art_artists[len(art_artists)-1])-2]
        model.addMedium_nationality(gallery,artwork,art_artists)
        model.addArtID(gallery,artwork,art_artists)

# Funciones de ordenamiento

def sortArtworks(gallery, size, sort_type):
    return model.sortArtworks(gallery, size, sort_type)

def sortArtist(gallery,sorted_artists):
    nations = initArtists()
    for i in range(lt.size(gallery["artwork"])):
        model.sortArtist(gallery,nations,lt.getElement(gallery["artwork"],i),sorted_artists)
    return nations

def best_artists(artist_nations):
    return model.sortArtistsbyNation(artist_nations)

def sortByArtistID(gallery):
    return model.sortByArtistID(gallery)

def sortByArtistName(gallery):
    return model.sortByArtistName(gallery)

def encontrar_ID(gallery,value):
    return model.buscar_id(gallery,value)
    
def requ4(objeto):
    return model.requerimiento_4(objeto)

    
# Funciones de consulta sobre el catálogo

def requerimiento_1(gallery,ai,af):
    return model.requerimiento_1(gallery,ai,af)
def requerimiento_2(gallery,fi,ff):
    return model.requerimiento_2(gallery,fi,ff)
def requerimiento_3(gallery,name):
    return model.requerimiento_3(gallery,name)
def contar_tecnica(data):
    return model.contar_tecnica(data)
def obras_departamento(gallery, department):
    return model.obras_departamento(gallery,department)
def estimar_valor(obras):
    return model.estimar_valor(obras)
def obras_antiguas(departamento):
    return model.obras_antiguas(departamento)
def obras_costosas(departamento):
    return model.obras_costosas(departamento)

def requerimiento_5(gallery,department):
    return model.requerimiento_5(gallery,department)

def obtener_id(gallery,name):
    return model.obtener_id(gallery,name)

def ReqLab5(gallery,medium):
    result = model.ReqLab5(gallery,medium)
    return result

def bono(gallery, artistas):
    return model.bono(gallery, artistas)

def obtener_obras_nacionalidad(gallery, nacionalidad):
    return model.obtener_obras_nacionalidad(gallery, nacionalidad)

def n_obras(lista, n):
    return model.n_obras(lista,n)

