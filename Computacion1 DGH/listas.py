#Ejercicio 1
print('Ejercicio 1')
inp=[3,234,534,12,34,65]
out=[]
t=0
for n in inp:
    t=(0.003*n**3)+2
    out.append(t)
print(out)
print()

#Ejercicio 2
print('Ejercicio 2')
cad='''batman,uses technology,superman,flies through the air,spiderman,uses a web,ghostrider,rides a motorcycle '''
palabra=''
salida=[]
for n in range(len(cad)):
    if cad[n]==',' or n==(len(cad)-1):
        salida.append(palabra)
        palabra=''
    else:
        palabra+=cad[n]
print(salida)

# Ejercicio 3
print('\n'+'Ejercicio 3')
cad2=''
for n in salida:
    cad2+=n+'**'
print(cad2)

# Ejercicio 4
cortado=[]
print('\n'+'Ejercicio 4')
for n in range(len(cad)):
    if (n+1)%5==0 or n==len(cad)-1:
        palabra+=cad[n]
        cortado.append(palabra)
        palabra=''
    else:
        palabra+=cad[n]
print(cortado)

# Ejercicio 5
print('\n'+'Ejercicio 5')
calif=[6, 7, 5, 9, 10]
def prom(Lista):
    p=0
    for n in Lista:
        p+=n
    prom=p/len(Lista)
    return prom
def mayor(Lista):
    m=0
    for n in Lista:
        if n>m:
            m=n
    return m
def menor(Lista):
    m=10
    for n in Lista:
        if n<m:
            m=n
    return m
calif.append(prom(calif))
calif.append(mayor(calif))
calif.append(menor(calif))
print(calif)

# Ejecicio 6
from random import randint
print('\nEjercicio 6')
randnum=[]
def ale(lista, x):
    for n in range(x):
        x=randint(1,100)
        lista.append(x)
ale(randnum, 10)
print(randnum)

o=[]
for n in range(len(randnum)):
    o.append(mayor(randnum))
    randnum.remove(mayor(randnum))
print(o)
# Ejercicio 7
print('\nEjercicio 7')
l1=[]
ale(l1, 5)
print(l1)
l2=[]
ale(l2, 5)
print(l2)
l3=[]
for n in range(5):
    s=l1[n]+l2[n]
    l3.append(s)
print(l3)

# Ejercicio 8
print('\nEjercicio 8')
def cuadro(b, h):
    for n in range(h):
        if n==0 or n ==h-1:
            print('1'*b)
        else:
            print('1'+('0'*(b-2))+'1')
cuadro(15, 5)