import random
numb = random.randrange(1, 6)
print('Estou pesando em um numero de 0 a 5, teste acertar')
acert = int(input('Digite o numero: '))
if acert == numb:
    print('{} Parabens vc acertou'.format(numb))
else:
    print('Vc errou o numero que estava pensando era {} '.format(numb))