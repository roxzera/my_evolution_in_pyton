s = 0
a = 0
for c in range(0, 500+1):
    if c % 2 == 1:
        if c % 3 == 0:
            a += 1
            s += c
print('Os numeros impares que sao multiplos por 3 somados sao {}, tem um total de {}: '.format(s, a))
