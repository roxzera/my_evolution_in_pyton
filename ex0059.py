num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
maiornumero = 0
menu = 0
while menu != 5:
    print('=-'*5, 'MENU', '-='*5)
    print('[ 1 ] Soma')
    print('[ 2 ] Multipicação')
    print('[ 3 ] Maior numero')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair')
    menu = int(input(''))
    if menu == 1:
        print('A soma do {} e do {} e de: {}'.format(num1, num2, num1 + num2))
    elif menu == 2:
        print('A multipicação do {} e do {} e de: {}'.format(num1, num2, num1*num2))
    elif menu == 3:
        if num1 > num2:
            maiornumero = num1
        else:
            maiornumero = num2
        print('O maior numero e {}'.format(maiornumero))
    elif menu == 4:
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('\033[31mOpcao invalida\033[m')
print('=-'*3, 'FIM DO MENU!', '-='*3)
