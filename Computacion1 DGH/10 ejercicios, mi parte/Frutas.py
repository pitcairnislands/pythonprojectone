lista={
    'platano':1.35,
    'manzana':0.8,
    'pera':0.85,
}
test=True
while test:
    f=input('Introduzca fruta: ').lower()
    if f=='platano' or f=='manzana' or f=='pera':
        break
    else:
        print('Fruta no existente, intente de nuevo')

k=int(input('Numero de kilos: '))
    
print('Articulo: '+f)
print('Cantidad: '+str(k))
p=lista[f]*k
print('Precio: '+str(p))

        


    