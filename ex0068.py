from random import randint
venceu = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
while True:
    pc = randint(0, 11)
    num = int(input('Digite um valor: '))
    testador = str(input('Par ou impar? [P/I]: ')).strip().upper()[0]
    resultado = num + pc
    if resultado % 2 == 1:
        if testador in 'Pp':
            print('-'*40)
            print(f'Voce jogou {num} e o computador {pc}. Total de {resultado} DEU IMPAR')
            print('\nVoce \033[31mperdeu!\033[m')
            break
        if testador in 'Ii':
            print('-' * 40)
            print(f'Voce jogou {num} e o computador {pc}. Total de {resultado} DEU IMPAR')
            print('\nVoce \033[32mvenceu!\033[m ')
            print('-' * 40)
            venceu += 1
        else:
            print('\n\033[31mOpcao invalida\033[m\n')
    else:
        if testador in 'Pp':
            print('-' * 40)
            print(f'Voce jogou {num} e o computador {pc}. Total de {resultado} DEU PAR')
            print('\nVoce \033[32mvenceu!\033[m ')
            print('-' * 40)
            venceu += 1
        if testador in 'Ii':
            print('-'*40)
            print(f'Voce jogou {num} e o computador {pc}. Total de {resultado} DEU PAR')
            print('\nVoce \033[31mperdeu!\033[m')
            break
        else:
            print('\n\033[31mOpcao invalida\033[m\n')
print('-='*20)
print(f'GAME OVER! Voce venceu {venceu} vezes')
