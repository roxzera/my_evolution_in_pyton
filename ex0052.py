num1 = int(input('Digite um numero: '))
total = 0
for c in range(1, num1 + 1):
    if num1 % c == 0:
        print('\033[1;32m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end='')
if total == 2:
    print('\n\033[mO {} foi divisiveis {} por tres, \033[32mnumero primo\033[m'.format(num1, total))
else:
    print('\n\033[mO {} foi divisiveis {} por tres, \033[31mnao primo\033[m'.format(num1, total))
