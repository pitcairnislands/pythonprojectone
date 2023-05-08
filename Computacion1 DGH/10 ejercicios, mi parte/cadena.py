directorio="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

dsinpam=''
for n in range(len(directorio)):
    if directorio[n]=='\n':
        break
    dsinpam+=directorio[n]
param=dsinpam.split(';')
        
#print(param)
directorio=directorio.replace(dsinpam+'\n', '')
#print(directorio)
atr=directorio.split('\n')
#print(atr)
dic={}
for n in range(len(atr)):
    dic2={}
    v=atr[n].split(';')
    for k in range(len(param)-1):
            dic2[param[k+1]]=v[k+1]
    dic[v[0]]=dic2
print(dic)