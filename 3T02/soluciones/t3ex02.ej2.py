import mysql.connector

def datosPelicula(titulo):
    try:
        # conectamos a la base de datos
        connect = mysql.connector.connect(user='admin', password='1234', host='localhost', database='sakila')
        cursor = connect.cursor()
        # buscamos el código de la película
        sql = ("SELECT film_id from film WHERE title = '" + titulo + "'")
        cursor.execute(sql)
        resultado = cursor.fetchall()
        # solo me puede devolver un valor o cero puesto que film_id es clave primaria
        # si me devuelve 0 es que la película no está en la base de datos
        if len(resultado) == 0:
            print("La película", titulo,  "no está en la base de datos")
        else:
            # si me devuelve 1, tomo el código. Puesto que fetchall me devuelve una tupla de tuplas, la primera (la 0)
            # es la única. Como solo he peidodo una columna (el film_id) está en la posición 0 de la tupla
            print("Pelicula:", titulo)
            codigo = resultado[0][0]
            # Busco la descripción. Igualmente film_id es clave primaria, así que solo me devuelve un elemento
            # Considero que la base de datos es correcta y si la pelicula existe, también la descripción
            sql = ("SELECT description from film_text WHERE film_id = " + str(codigo))
            cursor.execute(sql)
            resultado = cursor.fetchall()
            print("Descripcion:", resultado[0][0])
            # Ahora busco el reparto. Lo hago con un JOIN entre las tablas actor y film_actor
            sql = ("SELECT first_name, last_name from actor JOIN film_actor WHERE actor.actor_id = film_actor.actor_id AND film_actor.film_id = " + str(codigo))
            cursor.execute(sql)
            # Aquí si me va a devolver mas de un valor, así que los proceso uno a uno y muestro los resultados en consola
            for (first_name, last_name) in cursor:
                print(last_name + ", " + first_name)
        # Finalmente cierro la base de datos
        cursor.close()
        connect.close()
    except mysql.connector.Error as err:
        print(err)

# probamos nuestra función con una peli buena y una mala
datosPelicula("LUCK OPUS")
datosPelicula("LO QUE EL VIENTO SE LLEVO")