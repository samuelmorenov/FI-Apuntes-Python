#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     30/11/2018
#-------------------------------------------------------------------------------
n=10
lista = n*[0]
for i in range(n):
    lista[i]=(i+1)**2
#------------------------
lista=[]
for i in range(n):
    lista.append((i+1)**2)
#------------------------
lista=[]
for i in range(n):
    lista = lista+[(i+1)**2]
#------------------------
lista=[(i+1)**2 for i in range(n)]
print lista
#-------------------------------------------------------------------------------
def nada(x):
    x=7

a=5
print a
nada(a)
print a
#-------------------------------------------------------------------------------
def nada2(x):
    x[0]=999

lista=[10,11,12,13,14]
print lista
nada2(lista)
print lista
#-------------------------------------------------------------------------------
def nada3(x):
    x[0]=7
    x[1]=False
    x[2]="hola"
    x.append(999)
    x=x+[888]

lista=[5,True,1.234]
nada3(lista)
print lista
#-------------------------------------------------------------------------------
"""Funciones para cadenas de caracteres:
len(-)
str(-)
chr(-)
ord(-)
max(-)
min(-)
list(-)
sorted(-)"""
cadena="Esto es una prueba"
print len(cadena)
print str(2**2)
print chr(65)
print ord("A")
print max(cadena) #sorted(cadena)[-1]
print min(cadena)
print list(cadena)
print sorted(cadena)
"""Operaciones para cadenas de caracteres:
*
+
in
[-]
[-:-] [:-] [-:]
[-:-:-] [:-:-] [-::-]
> >= < <= == !=
"""
print "Ana">"Juan"
print "aa">"a"
"""Metodos
split(-) #rompe la cadena de caracteres y el resultado lo devuelve como lista
join(-) #cadena.join(lista) concatena la lista con la cadena de por medio
find(-) #permite buscar la posicion de una cadena con respecto de otra
count(-) #permite contar cuantas veces esta una subcadena dentro de una cadena
strip(-) #elimina subcadenas por delante y por detras
lstrip(-) #elimina solo por la izquierda
rstrip(-) #elimina solo por la derecha
replace(-,-) #sustituye una subcadena por otra
"""
cadena="esto es\nuna prueba"
print cadena
print cadena.split()
print cadena.split(" ")
print cadena.split("\n")
print cadena.split("a")
print cadena.split("es")
lista=["hola","una","prueba"]
print " ".join(lista)
print cadena.find("es")
print cadena.find("es",0)
print cadena.find("es",1)
print cadena.find("es",2)
print cadena.find("no")
print cadena.count(" ")
cadena="         esto es una prueba     "
print "*"+cadena+"*"
print "*"+cadena.strip(" ")+"*"#por defecto es espacio en blanco
print "*"+cadena.lstrip()+"*"
print "*"+cadena.rstrip()+"*"
cadena=cadena.strip()
print cadena.replace("a","ooo")
print cadena.replace("a","ooo").replace(" ","-")

