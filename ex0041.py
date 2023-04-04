from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano que nasceu: '))
idade = ano_atual - ano_nasc
print('O atetla tem {} Anos.'.format(idade))
if idade <= 9:
    print('Classificação: Sênior')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Júnior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
