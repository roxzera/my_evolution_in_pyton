a = int(input('Digite o primeiro numero da PA? '))
b = int(input('Digite a PA? '))
decima = a + (10-1) * b
for c in range(a, decima + b, b):
    print(c, end=' - ')
print('Acabou')
