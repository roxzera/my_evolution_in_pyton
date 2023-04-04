from random import randint
from time import sleep
tentativas = 1
pc = randint(1, 10)
print('*****************')
print('JOGO DE ADIVINHAR')
print('*****************')
print('Estou pensando em um numero de 0 a 10, tente acertar')
sleep(1)
for c in range(0, 3):
    print(f'Voce tem {tentativas} tentativas de 3')
    acertou = int(input('Digite um numero: '))
    if acertou < 1 or acertou > 10:
        print('Numero invalido digite um numero de 1 a 10')
        continue
    if acertou == pc:
        print('Voce acertou')
        break
    else:
        if acertou > pc:
            print('Voce digitou um numero maior doque eu pensei... tente novamente!')
            sleep(1)
        elif acertou < pc:
            print('Voce digitou um numero menor doque eu pensei... tente novamente!')
    tentativas += 1
