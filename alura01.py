print('*****************************')
print('Bem vindo ao jogo do adivinha')
print('*****************************')
numero = 45
cont = 0
tentativas = 1
while cont < 3:
    print(f'Voce tem {tentativas} de 3')
    acertou = int(input('Digite um numero: '))
    if numero == acertou:
        print('Parabens vc acertou')
        break
    else:
        if acertou > numero:
            print('Voce chutou mais alto, tente novamente')
        elif acertou < numero:
            print('Voce chutou mais baixo, tente noavente')
    cont += 1
    tentativas += 1
print('Fim de programa')
