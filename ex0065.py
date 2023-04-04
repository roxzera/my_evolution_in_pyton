somador = 0
num = 0
quantidade = 0
media = 0
maior = 0
menor = 0
continuar = ''
while continuar != 'N':
    num = int(input('Digite um numero: '))
    if quantidade == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num > menor:
        menor = num
    quantidade += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    somador += num
media = somador / quantidade
print('A soma de {} digitado foi de {}'.format(quantidade, somador))
print('Media: ', media)
print('Maior numero digitado ', maior)
print('Menor numero digitado ', menor)
