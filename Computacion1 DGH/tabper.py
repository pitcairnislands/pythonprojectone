tp=[
    {
        'elemento':'hidrogeno',
        'num atom':1,
        'simbolo':'H',
        'valencia':'1',
    },
    {
        'elemento':'Helio',
        'num atom':2,
        'simbolo':'He',
        'valencia':2,
    },
    {
        'elemento':'Litio',
        'num atom':3,
        'simbolo':'Li',
        'valencia':1,
    },
    {
        'elemento':'Berilio',
        'num atom':4,
        'simbolo':'be',
        'valencia':2,
    },
    {
        'elemento':'Boro',
        'num atom':5,
        'simbolo':'B',
        'valencia':1,
    },
    {
        'elemento':'Carbono',
        'num atom':6,
        'simbolo':'C',
        'valencia':2,
    },
    {
        'elemento':'Nitrogeno',
        'num atom':7,
        'simbolo':'N',
        'valencia':3,
    },
    {
        'elemento':'Oxigeno',
        'num atom':8,
        'simbolo':'O',
        'valencia':4,
    },
    {
        'elemento':'Fluor',
        'num atom':9,
        'simbolo':'F',
        'valencia':5,
    },
    {
        'elemento':'Neon',
        'num atom':10,
        'simbolo':'Ne',
        'valencia':6,
    }
]
for a in tp:
    print(a['elemento']+'-'+str(a['num atom']))