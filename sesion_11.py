#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     14/12/2018
#-------------------------------------------------------------------------------

def pasarSegundosAHoras(t):
    if(t > 60*60):
        horas = int(t/60*60)
        minutos = int((t-horas)/60)
        segundos = t-(60*60*horas)-(60*minutos)
        return str(horas)+":"+str(minutos)+":"+str(segundos)
    if(t > 60):
        minutos = int(t/60)
        segundos = t-(minutos*60)
        return str(minutos)+":"+str(segundos)
    return str(t)

def segundos(t):
    tiempo = t.split(":")
    horas = int(tiempo[0])
    minutos = int(tiempo[1])
    segundos = float(tiempo[2])
    return segundos + (minutos*60) + (horas*60*60)

def ejercicio1():
    """
    En un fichero llamado "descenso_del_sella.txt" se dispone de los datos de los
    principantes en K1 del descenso del sella, en cada linea esta el nombre completo
    del participante, seguido de una coma, y el tiempo invertido en el descenso
    expresado en horas, minutos y segundos con decimas (hh:mm:ss,s) un ejemplo de las
    primeras lineas seria:

    Luis Amado Perez Blanco, 1:15:31.5
    Jonh Smith, 1:17:22.4
    Jose Julian Becerro, 1:15:22.7
    Sebastian Mulier, 1:16:43.0
    Federico Vega Suarez 1:15:28.3

    Haga un programa que permita obtener el nombre del vencedor y la diferencia de
    tiempos entre el vencedor y el ultimo en entrar en la meta.
    """
    fichero=open("descenso_del_sella.txt","r")
    todo=fichero.readlines()
    fichero.close()

    tiempoMayor = 0
    tiempoMenor = -1

    for e in todo:
        datos = e.split(",")
        nombre = datos [0]
        tiempoTotal = segundos(datos[1])

        if(tiempoMenor == -1):
            tiempoMenor = tiempoTotal

        if(tiempoTotal > tiempoMayor):
            mayor = nombre
            tiempoMayor = tiempoTotal

        if(tiempoMenor > tiempoTotal):
            menor = nombre
            tiempoMenor = tiempoTotal


    print "El vencedor es:",menor
    print "La diferencia de tiempos entre el vencedor y el ultimo ha sido de",
    print tiempoMayor-tiempoMenor, "segundos"

def ejercicio2():
    """
    Escribe un programa tal que dado un fichero de texto genere otro con las
    lineas en orden inverso. Todas las lineas deben acabar en el terminador de
    linea \n incluso si no existe en la ultima linea del fichero original

    Los nombres de ambos ficheros deben pedirse por teclado

    Ejemplo de fichero original

    Esto es una prueba,
    aqui va la segunda linea
    luego la tercera
    y se acaba el fichero

    Nuevo fichero generado

    y se acaba el fichero
    luego la tercera
    aqui va la segunda linea
    Esto es una prueba,
    """
    nombreOriginal = "test.txt"#raw_input("Introduzca el nombre del fichero original:")
    fO = open(nombreOriginal,"r")
    todo=fO.readlines()
    fO.close()

    nombreGenerado = "test.txt"#raw_input("Introduzca el nombre del fichero a generar:")
    fG = open(nombreGenerado, "w")
    for i in range(len(todo)-1,-1,-1):
        fG.write(todo[i].strip("\n")+"\n")
    fG.close()

ejercicio1()
ejercicio2()



