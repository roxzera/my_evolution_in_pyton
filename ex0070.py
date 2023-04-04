total = mil = menor = 0
cont = 1
menornome = ''
while True:
    nome = str(input('Digite nome do produto: ')).strip()
    preco = float(input('Preco do produto R$: '))
    total += preco
    if preco > 1000:
        mil += 1
    if cont == 1:
        menor = preco
        menornome = nome
    else:
        if preco < menor:
            menor = preco
            menornome = nome
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('Fim do programa! ')
        break
print(f'Total a ser gasto e de {total}R$')
print(f'Total de produto que custa mais de mil reais {mil}')
print(f'O menor preco e o {menornome} custando {menor}')
