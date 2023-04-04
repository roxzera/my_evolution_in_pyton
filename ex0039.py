from datetime import date
ano_nasc = int(input('Qual ano voce nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 18:
    ano_menor = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(ano_menor))
    print('Seu alistamento sera em {}'.format((ano_atual + ano_menor)))
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasc, idade, ano_atual))
elif idade == 18:
    print('Deve se alistar IMEDIATAMENTE!')
else:
    ano_maior = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(ano_maior))
    print('E seu alistamento foi em {}'.format((ano_nasc + ano_maior)))