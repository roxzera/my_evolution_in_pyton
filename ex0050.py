par = 0
s = 0
for c in range(0, 6+1):
    digite = int(input('Digite um numero: '))
    if digite % 2 == 0:
        par += 1
        s += digite
print('O total de pares digitados foi {}, e eles somados foram {}'.format(par, s))
