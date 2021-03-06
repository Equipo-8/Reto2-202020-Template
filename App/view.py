"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config
from time import process_time 

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


castingfile = 'MoviesCastingRaw-small.csv'
moviesfile = 'SmallMoviesDetailsCleaned.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


def printMoviesByProducer(producer):
    
    if producer:
        print('Productor encontrado: ' + producer['name'])
        print('Promedio: ' + str(producer['vote_average']))
        print('Total de películas: ' + str(lt.size(producer['movies'])))
        iterator = it.newIterator(producer['movies'])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['original_title'] + '  Id: ' + book['id'])
    else:
        print('No se encontro el autor')

def printMoviesByDirector(director):
    
    if director:
        print('Director encontrado: ' + director['name'])
        print('Promedio: ' + str(director['vote_average']))
        print('Total de películas: ' + str(lt.size(director['movies'])))
        iterator = it.newIterator(director['movies'])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['original_title'] + '  Id: ' + book['id'])
    else:
        print('No se encontro el director')

def printMoviesBygenre(genre,needoflist):
    
    if genre:
        print('Género encontrado: ' + genre['name'])
        print('Promedio: ' + str(genre['vote_average']))
        print('Total de películas: ' + str(lt.size(genre['movies'])))
        if needoflist:
            iterator = it.newIterator(genre['movies'])
            while it.hasNext(iterator):
                book = it.next(iterator)
                print('Titulo: ' + book['original_title'] + '  Id: ' + book['id'])
    else:
        print('No se encontro el género '+genre)

def printMoviesBycountrie(countrie,needoflist):
    
    if countrie:
        print('Género encontrado: ' + countrie['name'])
        print('Promedio: ' + str(countrie['vote_average']))
        print('Total de películas: ' + str(lt.size(countrie['movies'])))
        if needoflist:
            iterator = it.newIterator(countrie['movies'])
            while it.hasNext(iterator):
                book = it.next(iterator)
                print('Titulo: ' + book['original_title'] + '  Id: ' + book['id' ]+' Director: '+ book['director'] + " Fecha de Producción: "+ book["release_date"])
    else:
        print('No se encontro el género '+countrie)

def printMoviesByActor(actor):
    
    if actor:
        print('Actor encontrado: ' + actor['name'])
        print('Promedio: ' + str(actor['vote_average']))
        print('Total de películas: ' + str(lt.size(actor['movies'])))
        print('Director con más colaboraciones: '+ actor["most"][0])
        print('Colaboraciones: '+ str(actor["most"][1]))
        iterator = it.newIterator(actor['movies'])
        while it.hasNext(iterator):
            book = it.next(iterator)
            print('Titulo: ' + book['original_title'] + '  Id: ' + book['id'])
    else:
        print('No se encontro el autor')


def printBooksbyTag(books):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
    iterator = it.newIterator(books)
    while it.hasNext(iterator):
        book = it.next(iterator)
        print(book['title'])


def printBooksbyYear(books):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
    iterator = it.newIterator(books)
    while it.hasNext(iterator):
        book = it.next(iterator)
        print(book['title'])


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información de las películas en el catálogo")
    print("3- Descubrir productoras de cine (individual)")
    print("4- Conocer a un director")
    print("5- Conocer a un actor")
    print("6- Entender un género cinematográfico")
    print("7- Encontrar películas por país")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        t1_start = process_time() #tiempo inicial
        controller.loadData(cont, moviesfile, castingfile)
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        print('Películas cargadas: ' + str(controller.moviesSize(cont)))

    elif int(inputs[0]) == 3:
        producer = input("Buscando películas de la productora?: ")
        t2_start = process_time() #tiempo inicial
        moviesproductor = controller.getMoviesByProducer(cont, producer)
        t2_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t2_stop-t2_start," segundos")
        printMoviesByProducer(moviesproductor)

    elif int(inputs[0]) == 4:
        directorname=input("Buscando películas de director?: ")
        t3_start=process_time()#tiempo inicial
        movies_director= controller.getMoviesByDirector(cont,directorname)
        t3_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t3_stop-t3_start," segundos")
        printMoviesByDirector(movies_director)
    elif int(inputs[0]) == 5:
        actorname=input("Buscando películas de actor?: ")
        t4_start=process_time()#tiempo inicial
        movies_actor= controller.getMoviesByActor(cont,actorname)
        t4_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t4_stop-t4_start," segundos")
        printMoviesByActor(movies_actor)
    elif int(inputs[0]) == 6:
        genrename=input("Buscando películas del género: ")
        needoflist=input("Necesitas saber la lista de películas del género?: Si/No: ")
        if needoflist.lower()=="si":
            needoflist=True
        elif needoflist.lower()=="no":
            needoflist=False
        t5_start=process_time()#tiempo inicial
        movies_genre= controller.getMoviesBygenre(cont,genrename.title())
        t5_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t5_stop-t5_start," segundos")
        printMoviesBygenre(movies_genre,needoflist)
    elif int(inputs[0]) == 7:
        countriename=input("Buscando películas del país: ")
        needoflist=input("Necesitas saber la lista de películas del país?: Si/No: ")
        if needoflist.lower()=="si":
            needoflist=True
        elif needoflist.lower()=="no":
            needoflist=False
        t5_start=process_time()#tiempo inicial
        movies_countries= controller.getMoviesBycountrie(cont,countriename.title())
        t5_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t5_stop-t5_start," segundos")
        printMoviesBycountrie(movies_countries,needoflist)
    else:
        sys.exit(0)
sys.exit(0)
