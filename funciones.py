def suma(a,b):
    suma = a + b
    resultado = suma
    return resultado 

def resta(a,b):
    resta = a - b
    resultado2 = resta
    return resultado2

def mult_lista(lista1):
    producto = 1
    for numero in lista1:
        producto *= numero
    return producto
numeros = [1,4,5,6]
print(mult_lista(numeros))

def sumalista(lista2):
    suma = 1 
    for numero in lista2:
        suma += numero
    return suma
listanum = [8,6,2,4,4]
print(sumalista(listanum))

tupla = ('Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Urano','Neptuno')
def convierteTupla(lista):
    lista = list(tupla)
    return lista
print(convierteTupla(tupla))

lista = ['10, 20, 30']
def conviertelista(cadena):
    string = ''.join(lista)
    return string
print(conviertelista(lista))




    







      




          
