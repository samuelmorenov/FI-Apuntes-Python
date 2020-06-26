import math
#Calculo del factorial de un numero
x = 5
##x=int(raw_input("Introduzca el numero: "))
numero = x
factorial = int(1)
while x > 0:
    factorial = factorial * x
    x -= 1
print "El factorial de", numero, "es", factorial

#Existencia del numero i
menosUno = complex(-1)
i = (menosUno)**(0.5)
j = 1j
print "tipo de i", type(i), "valor de i", i
print "tipo de j", type(j), "valor de j", j

x = (2.7182818284590452**(3.14159265359*1j))+1
print "e^(pi*i)+1 es:",x
print "Si pongo \n2.7182818284590452 \nsale:\n",2.7182818284590452

#Multiplicacion de 2 cadenas
print "hola "*5 ##no se puede hacer "hola"*"hola" :(