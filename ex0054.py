from datetime import date
a = date.today().year
b = 0
for c in range(0, 7):
    ano = int(input('Digite o ano que nasce? '))
    idade = a - ano
    if idade >= 21:
        b += 1
print('No total teve {} pessoas de maior!'.format(b))
