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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'producers': None,
                'movies': None,
                'movieIds':None,
                'directors':None,
                'casting': None,
                'castingID':None,
                'actors':None,
                'genres':None,
                'countries':None}

    catalog['movies'] = lt.newList('SINGLE_LINKED', comparemovieIds)
    catalog['producers'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareProducersByName)
    catalog['movieIds'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=compareProducersByName)
    catalog['directors'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareDirectorsByName)
    catalog['actors'] = mp.newMap(200,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=CompareActorByName)
    catalog['countries'] = mp.newMap(200,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=comparecountriesByName)
    catalog['casting'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareCastingNames)
    catalog['castingID'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareCastingIDS)
    catalog['genres'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=comparegenresByName)
    return catalog

def compareProducersByName(keyname, producer):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(producer)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
def comparegenresByName(keyname, genre):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(genre)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(director)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparecountriesByName(keyname, countrie):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(countrie)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
def CompareActorByName(keyname,actor):
    authentry = me.getKey(actor)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

# Funciones para agregar informacion al catalogo

def addMovies(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['movieIds'], movie['production_companies'], movie)

def addCasting(catalog, casting):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['casting'], casting)
    mp.put(catalog['castingID'], casting['id'], casting)


def addMovieProducer(catalog, producername, movie):  
    producers = catalog['producers']
    existproducer = mp.contains(producers, producername)
    if existproducer:
        entry = mp.get(producers, producername)
        producer = me.getValue(entry)
    else:
        producer = newProducer(producername)
        mp.put(producers, producername, producer)
    lt.addLast(producer['movies'], movie)

    authavg = producer['vote_average']
    movieavg = movie['vote_average']
    if (authavg == 0.0):
        producer['vote_average'] = float(movieavg)
    else:
        producer['vote_average'] = (authavg + float(movieavg)) / 2

def addMovieDirector(catalog, directorname, movie):
    directors = catalog['directors']
    existdirector = mp.contains(directors, directorname)
    if existdirector:
        entry = mp.get(directors, directorname)
        director = me.getValue(entry)
    else:
        director = newDirector(directorname)
        mp.put(directors, directorname, director)
    lt.addLast(director['movies'], movie)

    authavg = director['vote_average']
    movieavg = movie['vote_average']
    if (authavg == 0.0):
        director['vote_average'] = float(movieavg)
    else:
        director['vote_average'] = (authavg + float(movieavg)) / 2

def addMoviecountrie(catalog, countriename, movie,director):
    countries = catalog['countries']
    existcountrie = mp.contains(countries, countriename)
    if existcountrie:
        entry = mp.get(countries, countriename)
        countrie = me.getValue(entry)
    else:
        countrie = newcountrie(countriename)
        mp.put(countries, countriename, countrie)
    movie['director']=director
    lt.addLast(countrie['movies'], movie)

    authavg = countrie['vote_average']
    movieavg = movie['vote_average']
    if (authavg == 0.0):
        countrie['vote_average'] = float(movieavg)
    else:
        countrie['vote_average'] = (authavg + float(movieavg)) / 2

def addMoviegenre(catalog, genrename, movie):
    genres = catalog['genres']
    existgenre = mp.contains(genres, genrename)
    if existgenre:
        entry = mp.get(genres, genrename)
        genre = me.getValue(entry)
    else:
        genre = newgenre(genrename)
        mp.put(genres, genrename, genre)
    lt.addLast(genre['movies'], movie)

    authavg = genre['vote_average']
    movieavg = movie['vote_average']
    if (authavg == 0.0):
        genre['vote_average'] = float(movieavg)
    else:
        genre['vote_average'] = (authavg + float(movieavg)) / 2

def addMovieActor(catalog, actorname, movie, director):
    actors = catalog['actors']
    existactor = mp.contains(actors, actorname)
    if existactor:
        entry = mp.get(actors, actorname)
        actor = me.getValue(entry)
    else:
        actor = newActor(actorname)
        mp.put(actors, actorname, actor)
    lt.addLast(actor['movies'], movie)
    authavg = actor['vote_average']
    movieavg = movie['vote_average']
    if (authavg == 0.0):
        actor['vote_average'] = float(movieavg)
    else:
        actor['vote_average'] = (authavg + float(movieavg)) / 2
    if director in actor['director_collaborations']:
        actor['director_collaborations'][director]+=1
    else:
        actor['director_collaborations'][director]=0
    if actor['director_collaborations'][director]>actor["most"][1]:
        actor["most"][0]=director
        actor["most"][1]=actor['director_collaborations'][director]

def newDirector(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    director = {'name': "", "movies": None,  "vote_average": 0}
    director['name'] = name
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return director

def newcountrie(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    countrie = {'name': "", "movies": None,  "vote_average": 0}
    countrie['name'] = name
    countrie['movies'] = lt.newList('SINGLE_LINKED', comparecountriesByName)
    return countrie

def newgenre(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    genre = {'name': "", "movies": None,  "vote_average": 0}
    genre['name'] = name
    genre['movies'] = lt.newList('SINGLE_LINKED', comparegenresByName)
    return genre

def newActor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    actor = {'name': "","movies": None, "vote_average": 0,"director_collaborations":{},"most":["None",0]}
    actor['name'] = name
    actor['movies'] = lt.newList('SINGLE_LINKED', compareActorsByName)
    return actor

def newProducer(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    producer = {'name': "", "movies": None,  "vote_average": 0}
    producer['name'] = name
    producer['movies'] = lt.newList('SINGLE_LINKED', compareProducersByName)
    return producer
    


# ==============================
# Funciones de consulta
# ==============================

def moviesSize(catalog):
    return lt.size(catalog['movies'])

def producersSize(catalog):
    return lt.size(catalog['producers'])

def directorsSize(catalog):
    return lt.size(catalog['directors'])

def actorsize(catalog):
    return lt.size(catalog['actor'])
# ==============================
# Funciones de Comparacion
# ==============================


def comparemovieIds(id1, id2):
    """
    Compara dos ids de libros
    """
    id1=int(id1)
    id2=int(id2)
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def getMoviesByProducer(catalog, producername):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    producer = mp.get(catalog['producers'], producername)
    if producer:
        return me.getValue(producer)
    return None


def getMoviesByDirector(catalog, directorname):
    
    director = mp.get(catalog['directors'], directorname)
    if director:
        return me.getValue(director)
    return None

def getMoviesBygenre(catalog, genrename):
    
    genre = mp.get(catalog['genres'], genrename)
    if genre:
        return me.getValue(genre)
    return None
def getMoviesBycountrie(catalog, countriename):
    
    countrie = mp.get(catalog['countries'], countriename)
    if countrie:
        return me.getValue(countrie)
    return None
def getMoviesByActor(catalog, actorname):
    actor = mp.get(catalog['actors'], actorname)
    if actor:
        return me.getValue(actor)
    return None

def compareCastingNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1

def compareActorsByName(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1

def compareCastingIDS(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0

def addMovieCasting(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = mp.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = mp.get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])

