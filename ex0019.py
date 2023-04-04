from random import choice
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digitar o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digitar o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
sorteador = choice(lista)
print('O nome sorteador foi {}'.format(sorteador))
