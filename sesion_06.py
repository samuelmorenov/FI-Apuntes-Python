#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     09/11/2018
#-------------------------------------------------------------------------------
#Tuplas:

mi_tupla="God",123456789,True
print mi_tupla, type(mi_tupla)
for elemento in mi_tupla:
    print elemento, type(elemento)

r=1,2,3
s=2*r+(4,5)
print s, type(s), len(s)
x,y,z=mi_tupla
print x,y,z
print
#-------------------------------------------------------------------------------
a=10
b=20
print a,b
c=a
a=b
b=c
print a,b
a,b=b,a
print a,b
print
#-------------------------------------------------------------------------------
from math import *
_pi = 3.14159265358979
a=sin(3.14159265358979/2)
print a
print cos(pi)
print exp(1)
print "\n"
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#Funciones:
from funciones_fi import *

def cubo(x):
    """Devuelve cubo de x"""
    return x*x*x


print cubo(2)
print
#-------------------------------------------------------------------------------
def suma(x,y):
    i=3
    print "i en la funcion", i
    return x+y

i=5
print suma(2,3)
print suma(1.5, 6.8)
print suma(2,3.5)
print suma("hola","test")
print "i en el programa principal", i
print
#-------------------------------------------------------------------------------
def es_mayor(a,b):
    """Devuelve si a es mayor que b"""
    return a>b

a=14
b=5
print es_mayor(a,b)
print es_mayor(10,12)
print es_mayor("Ana","Juan")
print es_mayor(False,True)
print "\n"
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#Funciones con tuplas:
def ordena(a,b):
    """Devuelve los parametros ordenados de menor a mayor"""
    if a<b:
        return a,b
    else:
        return b,a

def ordena2(a,b):
    """Devuelve los parametros ordenados de menor a mayor"""
    return min(a,b),max(a,b)

x,y=ordena(10,4)
print x,y
x,y=ordena2(5,22)
print x,y
print
#-------------------------------------------------------------------------------
def es_primo(numero):
    """Devuelve si es primo o no"""
    for divisor in range (2, numero):
        if numero%divisor==0:
            return False
    return True


for n in range(2,101):
    if es_primo(n):
        print n,


