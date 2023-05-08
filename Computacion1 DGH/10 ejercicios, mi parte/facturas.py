fact={
    '300':7500.0,
    #'301':79999.0,
    '302':650.0,
}
cobrado=0
salir=True
while salir:
    print('*'*10)
    print('Añandir factura: [1]')
    print('Pagar factura: [2]')
    print('Salir: [3]')
    print('Ver lista de facturas [4]')
    while True:

        act=(input())
        if act=='1' or act=='2' or act=='4':
            print('')
            break
        elif act=='3':
            salir=False
            break
        else:
            print('Introduzca accion valida')
            
    if act=='1':
        print('AÑADIR FACTURA')
        uso=True
        while uso:
            clave=(input('Introduzca clave nueva: '))
            if len(fact)==0:
                uso=False
            for n in range(len(fact)):
                if clave==str(list(fact.keys())[n]):
                    print('Clave ya en uso, introduzca otra')
                    uso=True
                    break
                else:
                    uso=False    
        cobro=float(input('Introduzca la cantidad del importe: $'))
        fact[clave]=cobro

    if act=='2':
        print('PAGAR FACTURA')
        ex=True
        while ex:
            clave=(input('Introduzca clave de la factura a pagar: '))
            for i in (fact):
                if clave==(i):
                    ex=False
                    break
                else:
                    ex=True
            if ex==True:
                print('Clave no encontrada')

        print('Factura '+str(clave))
        print('A pagar: $'+str(fact[clave]))
        cobro=float(input('Introduzca la cantidad que desea pagar: $'))
        if fact[clave]<cobro:
            print('Cambio: $'+str(cobro-fact[clave]))
            cobro=fact[clave]
            fact.pop(clave)
        elif fact[clave]==cobro:
            fact.pop(clave)
        else:
            fact[clave]-=cobro
            print('\n'+'Por pagar: $'+str(fact[clave])+'\n')
        cobrado+=cobro

    if act=='4':
        print('FACTURAS')
        if len(fact)==0:
            print('No hay facturas por cobrar')
        for i in (fact):
            print('-----')
            print('Clave: '+str(i))
            print('$'+str(fact[i]))

    print('')
    suma=0
    for i in fact:
        suma+=fact[i]
    print('Por cobrar: $'+str(suma))
    print('Cobrado: $'+str(cobrado)+'\n')