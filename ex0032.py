from datetime import date
ano = float(input('Digite 0 se quiser o ano atual, digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{:.0f} e um ano bissexto'.format(ano))
else:
    print('{:.0f} nao e um ano bissexto'.format(ano))