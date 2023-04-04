a = 0
menor_peso = 0
for c in range(1, 5+1):
    peso = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        menor_peso = peso
        a = peso
    else:
        if peso > a:
            a = peso
        elif peso < menor_peso:
            menor_peso = peso

print('{} MAIOR, {} MENOR'.format(a, menor_peso))
