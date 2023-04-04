from random import randrange
from time import sleep
numeropc = randrange(1, 11)
print('Estou pensando em numero de 1 a 10, tente acertar')
numeropessoa = int(input('Digite um numero: '))
print('Processando.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
tentativa = 1
while numeropessoa != numeropc:
    if numeropessoa > numeropc:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    #print('\033[31mVoce errou\033[m, tente novamente!')
    numeropessoa = int(input('Digite outro numero: '))
    tentativa += 1
    print('Processando.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)
print('\033[32mParabens \033[mvoce acertou, voce tentou {} vezes'.format(tentativa))