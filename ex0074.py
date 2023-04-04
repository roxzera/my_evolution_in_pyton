from random import randint
tubla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = 0
menor = 999
for c in tubla:
    print(c, end=' ')
    if c < menor:
        menor = c
    elif c > maior:
        maior = c
print(f'\nO maior e o {maior}')
print(f'O menor e o {menor}')
