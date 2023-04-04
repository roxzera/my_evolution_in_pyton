media = 0
idades = 0
maior = 0
maiorNomeHomem = ''
mulher20anos = 0
for p in range(1, 5):
    print('==== {} PESSOA ===='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    idades += idade
    if p == 1 and sexo == 'M':
        maior = idade
        maiorNomeHomem = nome
    if idade > maior and sexo == 'M':
        maiorNomeHomem = nome
        maior = idade
    if idade < 20 and sexo == 'F':
        mulher20anos += 1
media = idades / 4
print('A media das idade e de {:2f} anos'.format(media))
print('O total de mulheres com menos de 20 anos e {}'.format(mulher20anos))
print('O nome do homem com maior idade e o {} com {} anos'.format(maiorNomeHomem, maior))

