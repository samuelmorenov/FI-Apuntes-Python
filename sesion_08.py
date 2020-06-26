#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     23/11/2018
#-------------------------------------------------------------------------------
lista=[x**3/5. for x in range(100) if x%7==0 or x%3==0]
for i in lista:
    print i,
#-------------------------------------------------------------------------------
top=1000
no_primos=[j for i in range(2,int(top**0.5)) for j in range(i*2,top,i)]
##print no_primos
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt

## plt.plot([x**2/100. for x in range(100)])
## plt.show()
# Necesitas tener el modulo instalado

#-------------------------------------------------------------------------------
lista = [1,2,3,4,5,6,7,8,9]
#funciones
print len(lista)#cuantos caracteres hay en la lista
print max(lista)#maximo
print min(lista)#minimo
print sum(lista)#suma
print list(lista)#convierte a entero
#operadores
lista = lista+lista#concatena
lista = lista*8#repite 8 veces
e = 2
i = 2
e in lista#permite saber si el elemento esta en la lista
lista[i]#acceso al elemento i de la lista [-][-:-][-:-:-]
#metodos
lista.append(i)#añade un elemento a la lista
x = lista.pop(i)#quita un elemento de la lista y lo devuelve
lista.pop()#quita el ultimo elemento de la lista
lista.remove(e)#Extrae por valor, no devuelve nada
lista.insert(e,i)#inserta el elemento e en la posicion i
lista.index(e)#devuelve la posicion de un elemento en la lista
#-------------------------------------------------------------------------------
lista=[10,11,12]
lista.append(999)
print lista

lista=[10,11,12]
lista=lista+[999] #Cuidado que el puntero apunta a una nueva lista
print lista
#-------------------------------------------------------------------------------
cadena="una cadena"
lista=list(cadena)
print lista
#-------------------------------------------------------------------------------