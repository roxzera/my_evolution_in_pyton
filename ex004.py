a = input('Digite alguma coisa: ')
print('O tipo primitivo da variavel e: ', type(a))
print('E minusculo? ', a.islower())
print('E numero? ', a.isnumeric())
print('E letras? ', a.isalpha())
print('E letra e numeros? ', a.isalnum())
print('E numero flotoante? ', a.isdecimal())
print('Tem espaco? ', a.isspace())
print('TEm Maiusculo? ', a.isprintable())
print('esta capitarizada? ', a.istitle())