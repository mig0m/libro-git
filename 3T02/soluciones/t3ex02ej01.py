def construyeDiccionario(lista_animes):
    diccionario = {}
    for linea in lista_animes:
        # encontramos la posicion del primer espacio en blanco
        posicion = linea.find(" ")
        # a un lado y al otro del espacio están el código y el nombre
        codigo = linea[:posicion]
        nombre = linea[posicion + 1:]
        # eliminamos, si existe, el \n del final
        nombre = nombre.replace("\n", "")
        diccionario[codigo] = nombre
    return diccionario

def encuentraPersonajes(lista_personajes, codigoAnime):
    lista = []
    for linea in lista_personajes:
        # encontramos la posicion del primer espacio en blanco
        posicion = linea.find(" ")
        codigoPersonaje = linea[:posicion]
        if codigoAnime == codigoPersonaje:
            nombrePersonaje = linea[posicion + 1:]
            # eliminamos, si existe, el \n del final
            nombrePersonaje = nombrePersonaje.replace("\n", "")
            lista.append(nombrePersonaje)
    return lista

def encuentraPersonajesHuerfanos(lista_personajes, diccionario_animes):
    lista = []
    for linea in lista_personajes:
        # encontramos la posicion del primer espacio en blanco
        posicion = linea.find(" ")
        codigoPersonaje = linea[:posicion]
        # si el codigo del personaje no está en el diccionario de animes lo metemos en la lista que vamos a devolver
        if diccionario_animes.get(codigoPersonaje) == None:
            nombrePersonaje = linea[posicion + 1:]
            nombrePersonaje = nombrePersonaje.replace("\n", "")
            lista.append(nombrePersonaje)
    return lista

def salidaEnFichero(diccionario_animes, lista_personajes):
    try:
        with open('resultado.txt', "w") as fresultado:
            # procesamos linea a linea el diccionario
            for codigo, nombre in diccionario_animes.items():
                # encontramos los personajes para ese anime
                personajes = encuentraPersonajes(lista_personajes, codigo)
                # y los grabamos en el fichero. Si no hay personajes mostramos un mensaje
                fresultado.write(nombre + "\n")
                if len(personajes) > 0:
                    for personaje in personajes:
                        fresultado.write("- " + personaje + "\n")
                else:
                    fresultado.write("- No hay personajes" + "\n")
            # ahora procesamos a los personajes sin anime
            personajes_sin_anime = encuentraPersonajesHuerfanos(lista_personajes, diccionario_animes)
            if len(personajes_sin_anime) > 0:
                fresultado.write("Personajes sin anime" + "\n")
                for personaje in personajes_sin_anime:
                    fresultado.write("- " + personaje + "\n")
        print("Ficheros procesados con éxito. La salida está en el fichero resultado.txt")
    except:
        print("Error al procesar el fichero resultado.txt")


# leemos los dos ficheros y metemos en listas el contenido de cada uno de ellos
try:
    with open('animes.txt') as fanimes:
        lista_animes = fanimes.readlines()
except:
    print("Error al procesar el fichero animes.txt")
try:
    with open('personajes.txt') as fpersonajes:
        lista_personajes = fpersonajes.readlines()
except:
    print("Error al procesar el fichero personajes.txt")

# construimos un diccionario con los animes
diccionario_animes = construyeDiccionario(lista_animes)
# y procesamos el diccionario de animes y la lista de personajes
salidaEnFichero(diccionario_animes, lista_personajes)


