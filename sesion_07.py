#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     16/11/2018
#-------------------------------------------------------------------------------
from funciones_fi import *
for i in range(50):
    if i == 3:
        break
    print i,
print
for i in range(8):
    if i == 3:
        continue
    print i,
print
#-------------------------------------------------------------------------------
numero=500

for divisor in range(2,numero):
    if numero%divisor==0:
        print numero,"no es primo"
        break
else:
    print numero,"es primo"
#-------------------------------------------------------------------------------
esPrimo = True
divisor = 2
while divisor<numero and esPrimo:
    if numero%divisor==0:
        esPrimo=False
    divisor=divisor+1

if esPrimo:
    print numero,"es primo"
else:
    print numero,"no es primo"
#-------------------------------------------------------------------------------
def mostrar(coleccion):
    """muestra caracteristicas de la coleccion dada"""
    print "tipo",type(coleccion)
    print "numero de elementos", len(coleccion)
    print "elementos:"
    for elemento in coleccion:
        print elemento
    return 2*coleccion+coleccion

nueva=mostrar("hola")
print nueva
#-------------------------------------------------------------------------------
mi_tupla="Anna","Fernandez",987123456

nombre,apellido,telefono=mi_tupla
print mi_tupla
print nombre,apellido,telefono
#-------------------------------------------------------------------------------
cadena="hola" #cadena de caracteres
coleccion=(1,2,3,True) #coleccion
tuplas="Ana","Fernandez" #tublas
lista=[1,2,3,True] #lista
for elemento in coleccion:
    print elemento,
print
for i in range(len(coleccion)):
    print i,coleccion[i]

print
#-------------------------------------------------------------------------------
cadena="murcielago"
print cadena[3]
print cadena[3:7]
print cadena[3:7:2]
print cadena[7:3:-1]
print cadena[3:]
print cadena[:7]
print cadena[3:1000]
print cadena[::]
print cadena[::-1]
print cadena[-3]
print cadena[2:-3]
print
#-------------------------------------------------------------------------------
lista=[10,11,12,13,14,15,16,17,18,19]
lista[3]=333
print lista
lista[3:6]=[100,200,300,400,500]
print lista
lista[:3]=[]
print lista
lista[5:5]=["hola",True,6.7]
print lista
lista=[10,11,12,13,14,15,16,17,18,19]
lista[3:3]=lista
lista[3:3]=lista[::-1]
print lista