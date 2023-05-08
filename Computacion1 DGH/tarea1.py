#funciones
def cc(n): #coso para agregar gradualmente mas elementos, que usan 
    a=''
    for i in range(n):
        a=a+'·'
    return a
def cuadro(b,h):
    for i in range(h):
        print(cc(b))
def tri(b):
    for i in range(1,b):
        print(cc(i))
def tronco(b,h): #funcion extra para crear el tronco, que es basicamente cuadro pero con un espacio
    for i in range(h):
        print('', cc(b))

if __name__=="__main__":
    #cuadro
    print('CUADRO')
    cuadro(4,4)
    
    #triangulo
    print('\n','TRIANGULO')
    tri(5)
    
    #arbol flecha rara
    print('\n','IDK')
    tri(5)
    tronco(2,4)