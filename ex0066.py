cont = 0
soma = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitado {cont} e a soma deles e {soma}')
