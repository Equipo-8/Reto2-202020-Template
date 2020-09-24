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

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, moviesfile, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadMovies(catalog, moviesfile,castingfile)

def loadMovies(catalog, moviesfile, castingfile):
    """
    Carga cada una de las lineas del archivo de movies.
    - Se agrega cada movie al catalogo de movies
    - Por cada movie se encuentran sus autores y por cada
      autor, se crea una lista con sus movies
    """
    moviesfile = cf.data_dir + moviesfile
    input_file = csv.DictReader(open(moviesfile,encoding="utf-8-sig"),delimiter=";", quotechar='\"')
    castingfile = cf.data_dir +castingfile
    input_file2 = csv.DictReader(open(castingfile,encoding="utf-8-sig"),delimiter=";")
    for movie,casting in zip(input_file,input_file2):
        model.addMovies(catalog, movie)
        producers = movie['production_companies'].split(";")  # Se obtienen los autores
        model.addCasting(catalog, casting)
        directors = casting['director_name']
        actors = [casting['actor1_name'],casting['actor2_name'],casting['actor3_name'],casting['actor4_name'],casting['actor5_name']]
        genres = movie['genres'].split("|")
        countries = movie["production_countries"]
        for productor in producers:
            model.addMovieProducer(catalog, productor, movie)
        model.addMovieDirector(catalog, directors, movie)
        for actor in actors:
            model.addMovieActor(catalog,actor,movie,directors)
        for genre in genres:
            model.addMoviegenre(catalog,genre,movie)
        model.addMoviecountrie(catalog,countries,movie,directors)


def moviesSize(catalog):
    return model.moviesSize(catalog)

def getMoviesByProducer(catalog, producername):
    
    producerinfo = model.getMoviesByProducer(catalog, producername)
    return producerinfo

def getMoviesByDirector(catalog, directorname):

    director_info= model.getMoviesByDirector(catalog,directorname)
    return director_info

def getMoviesByActor(catalog,actorname):
     actor_info= model.getMoviesByActor(catalog,actorname)
     return actor_info

def getMoviesBygenre(catalog,genrename):
     genre_info= model.getMoviesBygenre(catalog,genrename)
     return genre_info
def getMoviesBycountrie(catalog,countriename):
     countrie_info= model.getMoviesBycountrie(catalog,countriename)
     return countrie_info