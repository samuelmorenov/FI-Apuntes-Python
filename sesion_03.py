#-------------------------------------------------------------------------------
# Author:      UO266321
# Created:     26/10/2018
#-------------------------------------------------------------------------------
"""
Comentario en
varias lineas

"""
#-------------------------------------------------------------------------------
a=1; b=2; c=3
#-------------------------------------------------------------------------------
test    \
     =\
     "hola" \
               *\
               8
#-------------------------------------------------------------------------------
ejemplo = 2.5
n=ejemplo#float(raw_input("numero"))
if n>0:
    absoluto=n
else:
    absoluto=-n
print "el valor absoluto de ",n,"es",absoluto
#-------------------------------------------------------------------------------
numero=ejemplo#float(raw_input("numero"))
if numero > 0:
    signo = 1
elif numero ==0:
    signo = 0
else:
    signo=-1
print "el signo de",numero,"es",signo
#-------------------------------------------------------------------------------
nota=ejemplo#float(raw_input("nota"))

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

print "la calificacion de ",nota,"es",calificacion
#-------------------------------------------------------------------------------
try:
    text="asd"#raw_input("numero a calcular el inverso")
    numero=float(text)
    inverso=1/numero
    print "el inverso de",numero,"es",inverso
except:
    print "no es posible calcular el inverso de",text
#-------------------------------------------------------------------------------
a=0
while True:
    print a
    a=a+1

print "fin"