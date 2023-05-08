mat=['mate', 'fisica', 'quimica', 'historia', 'lengua']
for n in range(len(mat)):
    cal=float(input('Introduzca su calificaion en '+mat[n]+': '))
    if cal>=6:
        mat[n]=''
print('\n'+'Usted necesita recursar:')
for i in mat:
    if i!='':
        print(i)