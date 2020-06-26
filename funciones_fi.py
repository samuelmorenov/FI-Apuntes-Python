#-------------------------------------------------------------------------------
# Name:        funciones
# Author:      UO266321
# Created:     09/11/2018
# Note:        Contiene las funciones de la sesion 1 a la 6
#-------------------------------------------------------------------------------
def factorial(x):
    """Calcula el factorial de x"""
    factorial = int(1)
    while x > 0:
        factorial = factorial * x
        x -= 1
    return factorial

def calificacion(nota):
    """Devuelve un string con la nota"""
    if nota <0 or nota >10:
        calificacion="invalida"
    elif nota<5:
        calificacion="suspenso"
    elif nota<7:
        calificacion="aprobado"
    elif nota<9:
        calificacion="notable"
    else:
        calificacion="sobresaliente"
    return calificacion

def calcularInverso(text):
    """Devuelve el inverso de un numero dado y si no lanza una excepcion"""
    try:
        numero=float(text)
        inverso=1/numero
        return inverso
    except:
        print "No es posible calcular el inverso de",text

def tieneRaiz(n):
    """Escribe si el numero n tiene raiz cubica exacta o no"""
    i=0
    while i*i*i<n:
        i=i+1
    if i*i*i==n:
        return "La raiz cubica de ",n,"es",i
    else:
        return n,"no tiene raiz cubica entera exacta"

def calcularPromedioPar(inferior, superior):
    """Ejercicio: Calcular el promedio de los numeros pares
    que hay entre 2 numeros dados"""
    suma=0
    contador=0

    for numero in range (inferior, superior+1):
        if numero%2==0:
            suma = suma + numero
            contador = contador+1
    promedio=float(suma)/contador
    return promedio

def raizDigital(n):
    """ Ejercicio  7
      Dado  un  numero  natural  n ,  escribe  un  programa  que  calcule  y
      muestre  la raiz  digital y  la persistencia aditiva de este.
      La persistencia aditiva es el numero de veces que hay que sumar los digitos
      de  un  numero,  inicialmente  el  numero n dado  y  en  sucesivas  veces
      la  suma  obtenida,  para  reducir  el resultado de esta a un unico digito.
      Ademas, este unico digito sera la raiz digital del numero n dado.
      Ejemplo : n = 2089
      Suma de digitos de    2089 = 19
      Suma de digitos de    19 = 10
      Suma de digitos de    10 = 1
      Salida del programa : La persistencia aditiva de 2089 es 3 y
      su raiz digital es 1"""
    raiz = n
    contador = 0;
    while raiz>9:
        raiz = str(raiz)
        suma = 0
        for i in raiz:
            suma += int(i)
        raiz = suma
        contador = contador + 1;
    return "La persistencia aditiva de", n, "es", contador,
    return "y su raiz digital es", raiz

def cubo(x):
    """Devuelve cubo de x"""
    return x*x*x

def es_mayor(a,b):
    """Devuelve si a es mayor que b"""
    return a>b

def ordena(a,b):
    """Devuelve los parametros ordenados de menor a mayor"""
    if a<b:
        return a,b
    else:
        return b,a

def ordena2(a,b):
    """Devuelve los parametros ordenados de menor a mayor"""
    return min(a,b),max(a,b)

def es_primo(numero):
    """Devuelve si es primo o no"""
    for divisor in range (2, numero):
        if numero%divisor==0:
            return False
    return True

def print_es_primo(numero):
    """Imprime si un numero es primo o no con break en el for"""
    for divisor in range(2,numero):
        if numero%divisor==0:
            print numero,"no es primo"
            break
    else:
        print numero,"es primo"

def print_es_primo2(numero):
    """Imprime si un numero es primo o no con uso de while"""
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

def mostrar_coleccion(coleccion):
    """muestra caracteristicas de la coleccion dada"""
    print "tipo",type(coleccion)
    print "numero de elementos", len(coleccion)
    print "elementos:"
    for elemento in coleccion:
        print elemento

def mostrar_lista(lista):
    lista.append("Nuevo append")
    print lista
    lista.insert(1,"Nuevo insert")
    print lista
    lista.remove("Nuevo append")
    print lista
    lista.pop(1)
    print lista

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

def archivoCSVRandom():
    from random import *
    fichero=open("datos2.csv","w")
    for i in range(20*3):
        fichero.write(str(randint(0,10))+";")
        if(i%3==2):
            fichero.write("\n")
    fichero.close()