#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     26/10/2018
#-------------------------------------------------------------------------------

n=25#int(raw_input("numero a evaluar si tiene raiz cubica"))

i=0

while i*i*i<n:
    i=i+1
#fin while


#-------------------------------------------------------------------------------
if i*i*i==n:
    print "la raiz cubica de ",n,"es",i
else:
    print n,"no tiene raiz cubica entera exacta"

#-------------------------------------------------------------------------------
for caracter in "hola":
    print caracter
#-------------------------------------------------------------------------------
print range(5,12,3)
#-------------------------------------------------------------------------------
print int(1000**(1/3.)), 1000**(1/3.)
#-------------------------------------------------------------------------------
##Ejercicio: Calcular el promedio de los numeros pares
## que hay entre 2 numeros que se piden por teclado
inferior=3#int(raw_input("numero inferior"))
superior=8#int(raw_input("numero superior"))

suma=0
contador=0

for numero in range (inferior, superior+1):
    if numero%2==0:
        suma = suma + numero
        contador = contador+1
promedio=float(suma)/contador
print "el numero es",promedio