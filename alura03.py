from random import randint
from time import sleep
numerofacil = randint(1, 20)
numeromedio = randint(1, 35)
numerodificil = randint(1, 50)
jogar = 0
print('*'*20)
print('  Jogo de adivinha')
print('*'*20)
print('''[1] = Facil
[2] = Medio
[3] = Dificil''')
print('*'*20)
nivel = int(input('Qual nivel de game voce vai querer? '))
if nivel == 1:
    print('-' * 50)
    print('Voce escolheu o modo facil, voce tera 10 tentativas!')
    sleep(1)
    print('Estou pensando em um numero de 1 a 20')
    sleep(1)
    print('Tente acertar')
    print('-' * 50)
    for facil in range(0 + 1, 10):
        print(f'Tentativa {facil} de {10}')
        jogar = int(input('Digite um numero: '))
        if jogar < 1 or jogar > 20:
            print('Numero invalido, digite um numero de 1 a 20!')
        if jogar == numerofacil:
            print('Parabens vc acertou')
            break
        else:
            if jogar > numerofacil:
                print('Um pouco menos... tente novamente!')
            elif jogar < numerofacil:
                print('Um pouco mais... tente novamente!')
    if jogar != numerofacil:
        print('Voce PERDEU!')
elif nivel == 2:
    print('-' * 50)
    print('Voce escolheu o modo facil, voce tera 5 tentativas!')
    sleep(1)
    print('Estou pensando em um numero de 1 a 35')
    sleep(1)
    print('Tente acertar')
    print('-' * 50)
    for medio in range(0 + 1, 6):
        print(f'Voce tem {medio} de {5}')
        jogar = int(input('Digite um numero: '))
        if jogar < 1 or jogar > 35:
            print('Numero invalido, digite um numero de 1 a 35!')
            continue
        if jogar == numeromedio:
            print('Voce venceu!')
            break
        else:
            if numeromedio > jogar:
                print('Um pouco mais... tente novamente!')
            elif numeromedio < jogar:
                print('Um pouco menos... tente novamente!')
    if numeromedio != jogar:
        print('Voce PERDEU!')
elif nivel == 3:
    print('-' * 50)
    print('Voce escolheu o modo facil, voce tera 3 tentativas!')
    sleep(1)
    print('Estou pensando em um numero de 1 a 50')
    sleep(1)
    print('Tente acertar')
    print('-' * 50)
    for dificil in range(1, 4):
        print(f'Voce tem {dificil} de {3}')
        jogar = int(input('Digite um numero: '))
        if jogar < 0 or jogar > 50:
            print('Numero invalido, digite um numero de 1 a 50')
        if jogar == numerodificil:
            print('Parabens voce acertou!')
            break
        else:
            if numerodificil > jogar:
                print('Um pouco mais... Tente novamente!')
            elif numerodificil < jogar:
                print('Um pouco menos... Tente novamente!')
    if jogar != numerodificil:
        print('Voce PERDEU!')
print('Fim do programa')
