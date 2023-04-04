print('='*8, 'LOJA BIFE', '='*8)
compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual opcão? '))
if opcao == 1:
    desconto = compras * 0.10
    total = compras - desconto
    print('Sua compra sera a vista, tera um desconto de {}R$'.format(desconto))
    print('E voce pagara no total {}R$'.format(total))
elif opcao == 2:
    desconto = compras * 0.05
    total = compras - desconto
    print('Sua compra sera a vista no cartao, e tera um desconto de {}R$'.format(desconto))
    print('E voce pagara no total {}R$'.format(total))
elif opcao == 3:
    parcelas = compras / 2
    print('Sua compra sera em 2 vezes sem juros no cartao, e voce pagara 2x de {}R$'.format(parcelas))
    print('E voce pagara no total de {}R$: '.format(compras))
elif opcao == 4:
    parcelas = int(input('Qual o numero de parcelas? '))
    desconto = (compras * 0.2) + compras
    total = desconto / parcelas
    print('Sua compra sera parcelada em {}x de {}R$'.format(parcelas, total))
    print('E pagara no total {}R$'.format(desconto))
else:
    print('Opção invalida!')


