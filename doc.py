import random
f = open('numeros.txt', 'w')
f.write('Esto es una libreria')
f.write('De distintas clases')
f.close()

f = open('numeros.txt', 'r')
lineas = f.readlines()
f.close()