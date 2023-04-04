from random import shuffle
n1 = str(input('Digitar o primeiro nome: '))
n2 = str(input('Digitar o segundo nome: '))
n3 = str(input('Digitar o terceiro nome: '))
n4 = str(input('Digitar o quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem sera ')
print(lista)
