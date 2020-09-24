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


catalogfile = 'MoviesCastingRaw-small.csv'
moviesfile = 'AllMoviesDetailsCleaned.csv'


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
        controller.loadData(cont, moviesfile)
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

    else:
        sys.exit(0)
sys.exit(0)
