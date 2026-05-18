
# comprueba que las listas de soluciones o de respuestas (son iguales) sean correctas
def comprobar(lista):
    correcto = True
    # Tiene que haber 10 respuestas
    if len(lista) != 10:
        correcto = False
    else:
        # y solo admitimos A, B, C o D como respuestas correctas
        for elemento in lista:
            if elemento not in ['A', 'B', 'C', 'D']:
                correcto = False
    return correcto

# Leemos las soluciones y comprobamos que el formato del fichero sea correcto
def leerSoluciones():
    soluciones = None
    try:
        with open("soluciones.txt") as f:
            texto = f.readline()
            # si hay \n lo eliminamos
            texto = texto.replace("\n","")
            soluciones = texto.split(", ")
            if comprobar(soluciones) == False:
                soluciones = None
    except:
        print("Error al procesar el fichero de soluciones")
        soluciones = None
    return soluciones

# calculamos la nota de cada examen
def calcularNota(soluciones, examen):
    nota = 0
    for i in range(0, len(soluciones)):
        if soluciones[i] == examen[i]:
            nota +=1
        else:
            nota -=0.3
    # La nota no puede ser negativa
    if nota < 0:
        nota = 0
    return nota

# procesamos las respuestas y hacemos un diccionario con los resultados
def procesarRespuestas(soluciones):
    notas = {}
    try:
        with open("respuestas.txt") as f:
            respuestas = f.readlines()
            for respuesta in respuestas:
                lista = respuesta.split(": ")
                alumno = lista[0]
                # si hay \n lo eliminamos
                lista[1] = lista[1].replace("\n", "")
                examen = lista[1].split(", ")
                if comprobar(examen) == True:
                    notas[alumno] = calcularNota(soluciones, examen)
    except:
        print("Error al procesar el fichero de respuestas")
        notas = None
    # si todas las respuestas son incorrectas o no hay respuestas devolvemos None
    if len(notas) == 0:
        print("El fichero de respuestas no tiene resultados válidos")
        notas = None
    return notas

def grabarNotas(resultados):
    try:
        with open("notas.txt", "w") as f:
            # procesamos el diccionario
            for elemento in resultados:
                # por cada elemento componemos una línea como la que nos piden y la grabamos en el fichero
                linea = elemento + ": " + str(resultados.get(elemento)) + "\n"
                f.write(linea)
    except:
        print("Error al procesar el fichero de notas")
    else:
        print("El fichero de notas se ha grabado correctamente")

# Aquí empieza el flujo del programa
# procesamos el fichero de solucions
soluciones = leerSoluciones()
if soluciones != None:
    # si es correcto procesamos los resultados de los alumnos
    resultados = procesarRespuestas(soluciones)
    # y si tenemos resultados válidos los grabamos en un fichero
    if(resultados!=None):
        grabarNotas(resultados)