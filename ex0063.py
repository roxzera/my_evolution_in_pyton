# 0  1  1 2 3 5
#       t1 t2
fibo = int(input('Digite ate onde quer mostrar a Sequência de Fibonacci: '))
t1 = 0
t2 = 1
cont = 3
print('{} - {}'.format(t1, t2), end='')
while cont <= fibo:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
