
while True:
    num = int(input('Digite o numero da taboada: '))
    if num < 0:
        print('Programa encerrado!')
        break
    for c in range(1, 11):
        print(f'{num} X {c} = ', num * c)
