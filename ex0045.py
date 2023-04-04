from random import randint
from time import sleep

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
escolha = int(input('Qual e sua jogada? '))
itens = ['Pedra', 'Papel', 'Tesoura']
jogada = randint(0, 2)
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO!!')
print('=-'*15)
print('O Computador escolha {}'.format(itens[jogada]))
print('Jogador jogou {}'.format(itens[escolha]))
print('=-'*15)
if jogada == 0: # computador jogando pedra
    if escolha == 0:
        print('\033[33mEMPATE')
    elif escolha == 1:
        print('Voce \033[32mganhou!\033[m')
    elif escolha == 2:
        print('Voce \033[31mperdeu!\033[m')
    else:
        print('OPCAO INVALIDA')
elif jogada == 1: # computador jogando papel
    if escolha == 0:
        print('Voce \033[31mperdeu\033[m')
    elif escolha == 1:
        print('\033[33mEmpate\033[m')
    elif escolha == 2:
        print('Voce \033[32mvenceu\033[m')
    else:
        print('\033[31mOPCAO INVALIDA\033[m')
elif jogada == 2: # computador jogando tesoura
    if escolha == 0:
        print('Voce \033[32mganhou\033[m')
    elif escolha == 1:
        print('Voce \033[31mperdeu\033[m')
    elif escolha == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('\033[31mOPCAO INVALIDA\033[m')

