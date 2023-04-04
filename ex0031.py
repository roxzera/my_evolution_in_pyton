passagem = float(input('Qual a distancia que era ir? '))
if passagem <= 200:
    preco = passagem * 0.45
    print('Voce vai pagar {:.2f}R$ em uma viagem de {}KM'.format(preco, passagem))
else:
    preco = passagem * 0.50
    print('Voce vai pagar {:.2f}R$ em uma viagem de {}KM'.format(preco, passagem))
