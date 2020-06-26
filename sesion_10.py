#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     07/12/2018
#-------------------------------------------------------------------------------
def reversa1(lista):
    nueva=[]
    for i in range(len(lista)-1,-1,-1):
        nueva.append(lista[i])
    return nueva

def reversa2(lista):
    nueva=[]
    for elemento in lista:
        nueva=[elemento]+nueva
    return nueva

def reversa3(lista):
    nueva=[]
    for elemento in lista:
        nueva.insert(0,elemento)
    return nueva

def reversa4(lista):
    nueva=[]
    for elemento in lista:
        nueva[:0]=[elemento]
    return nueva

def reversa5(lista):
    nueva=len(lista)*[0]
    for i in range(len(lista)):
        nueva[i]=lista[len(lista)-1-i]
    return nueva

def reversa6(lista):
    return lista[::-1]

def reversa7(lista):
    for i in range(len(lista)//2):
        aux=lista[i]
        lista[i]=lista[len(lista)-1-i]
        lista[len(lista)-1-i]=aux

def reversa8(lista):
    for i in range(len(lista)//2):
        lista[i],lista[len(lista)-1-i]=lista[len(lista)-1-i],lista[i]

def reversa9(lista):
    copia=list(lista)
    for i in range(len(copia)//2):
        copia[i],copia[-1-i]=lista[-1-i],copia[i]
    return copia

lista=[10,11,12,13]
##print reversa9(lista)
#-------------------------------------------------------------------------------
#Archivos
"""
Funciones:
open(-,-)
open(-) lectura
"w" escritura
"r" lectura
"a" añadir

Métodos
.write(-)
.readlines() #Devuelve una lista de lineas
.read() #Me lo guarda todo como una cadena de caracteres
.read(-) #el parametro indica el numero de caracteres a leer
.close()
"""
import funciones_fi
funciones_fi.archivoCSVRandom()
#-------------------------------------------------------------------------------
# crea un fichero cuyo nombre se pide por teclado y que contiene varias lineas
# escrito por Jose A. Corrales el 23-oct-2013

# antes de ejecutar el programa, salvarlo en el escritorio para
# que los ficheros se creen sobre el escritorio

# se pide por teclado el nombre del fichero
nombre_fichero="prueba.txt"#raw_input("nombre del fichero a crear (por ejemplo test.txt)")

# creacion del fichero al abrirlo para escritura
fichero=open(nombre_fichero,"w")

# proceso del fichero, se escribe un texto, numeros y el fin de linea
for i in range(5):
    j=i+1
    fichero.write("El inverso de "+str(j)+" es "+str(1.0/j)+"\n")

# se cierra el fichero
fichero.close()

print "fin del programa, mirar el fichero "+nombre_fichero
#-------------------------------------------------------------------------------
# lee el fichero prueba.txt entero y muestra su contenido
# escrito por Jose A. Corrales el 30-oct-2013

# antes de ejecutar el programa, salvarlo en el escritorio para
# que los ficheros deban estar sobre el escritorio

# se abre el fichero para lectura
fichero=open("prueba.txt")

# proceso del fichero, se lee todo como una lista de cadenas
lista=fichero.readlines()

# se cierra el fichero
fichero.close()

# se muestran los resultados
print lista

#-------------------------------------------------------------------------------
# lee el fichero prueba.txt entero y muestra su contenido
# escrito por Jose A. Corrales el 30-oct-2013

# antes de ejecutar el programa, salvarlo en el escritorio para
# que los ficheros deban estar sobre el escritorio

# se abre el fichero para lectura
fichero=open("prueba.txt")

# proceso del fichero, se lee todo en una unica cadena
todo=fichero.read().split("\n")#Añadido el split para quitar los \n

# se cierra el fichero
fichero.close()

# se muestran los resultados
print todo
#-------------------------------------------------------------------------------
fichero=open("prueba.txt")
todo=""
caracter=fichero.read(1)
while caracter!="":
    todo=todo+caracter
    caracter=fichero.read(1)
fichero.close()
print todo
#-------------------------------------------------------------------------------
fichero=open("prueba.txt")

# proceso del fichero, linea a linea
for linea in fichero:
    if linea[-1]=="\n":
        linea=linea[:-1]
    print linea
fichero.close()
