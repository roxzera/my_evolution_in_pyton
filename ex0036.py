casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario? '))
anos = int(input('Em quantos anos vai pagar? '))
valor_mensal = casa / (anos * 12)
porcetagem = salario * 0.3
if valor_mensal <= porcetagem:
    print('Emprestimo \033[32mACEITO!\033[m')
else:
    print('Emprestimo \033[31mNEGADO!\033[m')
print('Voce tera que pagar {:.2f}R$ em {} anos, 30% {}'.format(valor_mensal, anos, porcetagem))
