calc = 1
num_digitado = int(input('Qual taboada vc quer que eu mostre? '))
print('-='*10)
for c in range(1, 10+1):
    calc = c * num_digitado
    print('{} x {} = {}'.format(c, num_digitado, calc))
print('-='*10)
