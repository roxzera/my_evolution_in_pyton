velo = int(input('Digite a velocidade que estava? '))
if velo > 80:
    multa = (velo-80) * 7
    print('Voce esta a cima da velocidade da via')
    print('Tera que pagar uma multa de {}R$'.format(multa))
else:
    print('Voce esta dentro da velocidade estabelecida pela via')
