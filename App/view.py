"""
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
from DISClib.DataStructures import mapentry as me
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por nacionalidad de autor")
    print("6- Transportar obras de un departamento")
    print("7- Artistas más prolíficos")
    print("8- LAB 5: n OBRAS MÁS ANTIGUAS DE UN MEDIO")
    print("9- LAB 6: TOTAL DE OBRAS POR NACIONALIDAD")
    print("0- Salir")

gallery = None

def initGallery(type):
    return controller.initGallery(type)

def loadGallery(gallery):
    controller.loadData(gallery)


"""def printSorted(ord_gallery, sample_size=10):
    size = lt.size(ord_gallery)
    if size > sample_size:
        print("Las primeras", sample_size, "obras de arte ordenados son:")
        i = 1
        while i <= sample_size:
            artwork_1 = lt.getElement(ord_gallery,i)
            for k in artwork_1:
                print(f"{k}: {artwork_1[k]}")
"""
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        type = "ARRAY_LIST"
        gallery = initGallery(type)
        loadGallery(gallery)
        size_artists = lt.size(gallery["artists"])
        size_artworks = lt.size(gallery["artwork"])
        from DISClib.ADT import map as mp
        size_medium = mp.size(gallery["Medium"])
        size_ids = mp.size(gallery["ConstituentID"])
        print("Artistas cargados:",size_artists)
        print("Obras cargadas: ", size_artworks)
        print(f"Cantidad medios: {size_medium}")
        print(f"Cantidad Artistas: {size_ids}")
        print("Ultimos 3 artistas y obras: ")
        for i in range(1,4):
            print(f"\nArtista {i}")
            objeto_1 = lt.getElement(gallery["artists"],size_artists-i)
            for j in objeto_1:
                print("{}: {}".format(j, objeto_1[j]))
            print(f"\nObra {i}")
            objeto_2 = lt.getElement(gallery["artwork"],size_artworks-i)
            for k in objeto_2:
                print("{}: {}".format(k, objeto_2[k]))

        
    elif int(inputs[0]) == 0:
        break
    elif int(inputs[0]) == 2:
        #TODO View Requerimiento 1
        print("Busqueda de artistas por rango de años")
        ai = input("Digite el año inicial de la búsqueda: \n")
        af = input("Digite el año final de la busqueda: \n")
        lista = controller.requerimiento_1(gallery,ai,af)
        print(f"\nHay {lt.size(lista)} artistas nacidos en el rango {ai}-{af}")
        print("\nLos primeros 3 artistas son:\n")
        for i in range(3):
            actual = lt.getElement(lista,i)
            print(actual["DisplayName"],"\t",actual["BeginDate"],"\t",actual["EndDate"],"\t",actual["Gender"],"\t",actual["Nationality"])
        print("\nLos últimos 3 artistas son:\n")
        for i in range(3):
            actual = lt.lastElement(lista)
            print(actual["DisplayName"],"\t",actual["BeginDate"],"\t",actual["EndDate"],"\t",actual["Gender"],"\t",actual["Nationality"])
            lt.removeLast(lista)
        #Función en controller params : ai, af -> retorna [int,int,tuple(dict),tuple(dict)]
            
    elif int(inputs[0]) == 3:
        #TODO View Requerimiento 2
        print("Busqueda de adquisiciones por rango de fecha")
        fi = input("Digite la fecha inicial de la búsqueda: <AAAA-MM-DD>\n")
        ff = input("Digite la fecha final de la busqueda <AAAA-MM-DD>: \n")
        adquisiciones = controller.requerimiento_2(gallery,fi,ff)
        print(f"Hay {lt.size(adquisiciones[0])} obras adquiridas en el rango {fi}\t{ff}")
        print(f"\n{adquisiciones[1]} obras fueron compradas.")
        print("\nLas primeras 3 obras son:\n")
        
        for i in range(3):
            actual = lt.getElement(adquisiciones[0],i)
            art_artists = actual["ConstituentID"]
            artists = ""
            if not "," in art_artists:
                art_artists = art_artists[1:len(art_artists)-1]
                art_artists = [art_artists]
            else:
                art_artists = art_artists.split(",")
                art_artists[0] = art_artists[0][1:]
                art_artists[len(art_artists)-1] = art_artists[len(art_artists)-1][:len(art_artists[len(art_artists)-1])-2]
                for i in art_artists:
                    artista = controller.encontrar_ID(gallery, i)
                    artists += artista["DisplayName"]
            print(actual["Title"],"\t",artists,"\t",actual["Date"],"\t",actual["Medium"],actual["Dimensions"])
            print("\n\n")
        print("\n\nLas últimas 3 obras son:\n")
        for i in range(3):
            actual = lt.getElement(adquisiciones[0],lt.size(adquisiciones[0])-i)
            art_artists = actual["ConstituentID"]
            artists = ""
            if not "," in art_artists:
                art_artists = art_artists[1:len(art_artists)-1]
                art_artists = [art_artists]
            else:
                art_artists = art_artists.split(",")
                art_artists[0] = art_artists[0][1:]
                art_artists[len(art_artists)-1] = art_artists[len(art_artists)-1][:len(art_artists[len(art_artists)-1])-2]
                for i in art_artists:
                    artista = controller.encontrar_ID(gallery, i)
                    artists += artista["DisplayName"]
            print(actual["Title"],"\t",artists,"\t",actual["Date"],"\t",actual["Medium"],actual["Dimensions"])
            print("\n\n")
        #Función en controller params : fi, ff -> retorna [int,int,tuple(dict),tuple(dict)]       
    elif int(inputs[0]) == 4:
        #TODO View Requerimiento 3
        #try:
        print("="*8+"Clasificación de obras de artista por técnica"+"="*8)
        name = input("Digite el nombre del artista: \n")
        id_actual = controller.obtener_id(gallery,name)
        data = controller.requerimiento_3(gallery,id_actual) #Función en controller params: name -> retorna [int, int,str,list(dict)]
        data = me.getValue(data)
        print("="*8+"Examinar el trabajo del artista: "+name+"="*8)
        print(f"{name} tiene {lt.size(data)} obras a su nombre en el museo.")
        tecnicas = controller.contar_tecnica(data)
        tec = lt.getElement(tecnicas[0],0)["Medium"]
        print("\nSus técnicas con más obras son:")
        print("|\tTécnica\t|\t# de obras\t|")
        for i in range(10):
            actual = lt.getElement(tecnicas[1],i)
            print(f"|\t{actual[0]}\t|\t{actual[1]}\t|")
        print(f"Su técnica más utilizada es {tec} y se presentan a continuación ({lt.size(tecnicas[0])}):")
        separator = "-"*70
        table_format = "| {} | {} | {} | {} |"
        print(separator)
        print(table_format.format("Titulo","Fecha de la obra","Medio","Dimensiones"))
        for i in range(10):
            actual = lt.getElement(tecnicas[0],i)
            print(separator)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"]))
            print(separator)
        
    elif int(inputs[0]) == 5:
        #TODO View Requerimiento 4
        artistas_pais = gallery["Nationality"]
        print("\nObras catalogadas correctamente...")
        mejores = controller.requ4(artistas_pais)
        print("Los países con más obras según nacionalidad de su artista son:\n")
        print("País\t\tCantidad artistas")
        for i in range(1,10):
            elemento = lt.getElement(mejores,i)
            print(f"{elemento[0]}\t\t{elemento[1]}")
        mejor = lt.firstElement(mejores)[0]
        print(f"\n\nLas 3 primeras y últimas obras de autores {mejor} son:\n")
        print("""\tID\t|\tTitle\t|\tMedium\t|\tDate\t|\tDimensions\t|\tDepartment\t|
        \tClasification""")
        mejor_pais = mp.get(artistas_pais, mejor)
        obras_mejor_pais = me.getValue(mejor_pais)
        for i in range(3):
            actual = lt.getElement(obras_mejor_pais,i)
            print(actual["ObjectID"],"|\t",actual["Title"],"|\t",actual["Medium"],"|\t",actual["Date"],"|\t",actual["Department"],"|\t",actual["Classification"])
            print("\n")
        print("\n\n")
        for i in range(3):
            actual = lt.lastElement(obras_mejor_pais)
            print(actual["ObjectID"],"|\t",actual["Title"],"|\t",actual["Medium"],"|\t",actual["Date"],"|\t",actual["Department"],"|\t",actual["Classification"])
            lt.removeLast(obras_mejor_pais)

    elif int(inputs[0]) == 6:
        #TODO View Requerimiento 5
        print("Traslado de obras")
        department = input("Digite el nombre del departamento de dónde trasladar: \n")
        obras_departamento = controller.requerimiento_5(gallery,department)
        print(f"\nHay un total de {lt.size(obras_departamento)} obras para transportar")
        estimado = controller.estimar_valor(obras_departamento)
        print(f"\nEl costo estimado de transporte es de ${round(estimado,2)}")
        obras_antiguas = controller.obras_antiguas(obras_departamento)
        print("Las 5 obras más antiguas a transportar son:\n")
        table_format = "| {} | {} | {} | {} |"
        separator = "-"*70
        print(separator)
        print(table_format.format("Titulo","Fecha de la obra","Medio","Dimensiones"))
        for i in range(5):
            actual = lt.getElement(obras_antiguas,i)
            print(separator)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"]))
            print(separator)
        #Función en controller params: department -> retorna [int, int, float, list[dict],list[dict]]
        obras_costosas = controller.obras_costosas(obras_departamento)
        print("Las 5 obras más costosas a transportar son:\n")
        table_format = "| {} | {} | {} | {} | {} |"
        print(separator)
        print(table_format.format("Titulo","Fecha","Medio","Dimensiones","Costo transporte"))
        for i in range(5):
            actual = lt.getElement(obras_costosas,i)
            print(separator)
            f = round(actual["cost"],2)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"],f"${f}"))
            print(separator)
        op = input(f"Hay {lt.size(obras_departamento)} obras a ser transportadas, ¿desea visualizarlas?(Y/N): ")
        if op.lower() == "y":
            for i in range(lt.size(obras_departamento)):
                actual = lt.getElement(obras_departamento,i)
                print(separator)
                print(table_format.format(actual["Title"],actual["ConstituentID"],actual["Classification"],actual["Date"],actual["Medium"],actual["Dimensions"],actual["cost"]))
                print(separator)
        
              
    elif int(inputs[0])== 7:
        #TODO View Requerimiento 6 BONO
        numero_artistas = input("Ingrese cantidad de artistas que desea en la clasificación: ")
        ai = input("Ingrese año inicial de busqueda: ")
        af = input("Ingrese año final de busqueda: ")
        artistas = controller.requerimiento_1(gallery,ai,af)
        print(f"Hay {lt.size(artistas)} nacidos entre {ai} y {af}")
        obras = controller.bono(gallery,artistas)
        pass
    elif int(inputs[0]) == 3:
        size = int(input("Indique tamaño de la muestra: "))
        if size > lt.size(gallery["artwork"]):
            print("\nTamaño de muestra inválido.")
            continue
        print("\nSeleccione el método de ordenamiento a utilizar:")
        print("\n1 - Shellsort\n2 - Quicksort\n3 - Mergesort\n4 - Insertionsort")
        opt = input("\nOpción seleccionada: ")
        result = controller.sortArtworks(gallery, int(size), opt)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(round(result[0],2)))

        #printSorted(result[1])

    elif int(inputs[0]) == 8:
        medio = input("\nIngrese medio del que desea obtener obras: ")
        numero = int(input("\nIngrese el número de obras requeridas: "))
        objeto = controller.ReqLab5(gallery, medio)
        print(objeto)
        #mas_antiguas = controller.obras_antiguas(objeto)
        mas_antiguas = controller.n_obras(objeto, numero)
        print(f"Las {numero} obras más antiguas del medio {medio} son:")
        table_format = "| {} | {} | {} | {} |"
        separator = "-"*70
        print(separator)
        print(table_format.format("Titulo","Artista","Clasificacion","Fecha","Medio","Dimensiones","Costo transporte"))
        for i in range(lt.size(mas_antiguas)):
            actual = lt.getElement(mas_antiguas,i)
            print(separator)
            print(table_format.format(actual["Title"],actual["Date"],actual["Medium"],actual["Dimensions"]))
            print(separator)
    
    elif int(inputs[0]) == 9:
        nacionalidad = input("Ingrese la nacionalidad de la cual desea la cantidad de obras: ")
        obras = controller.obtener_obras_nacionalidad(gallery,nacionalidad)
        if obras != None:
            cantidad = lt.size(obras)
            print(f"La cantidad de obras de nacionalidad {nacionalidad} es {cantidad}")
        else:
            print("La nacionalidad indicada no se encuentra en ninguna obra")
    else:
        sys.exit(0)
sys.exit(0)
