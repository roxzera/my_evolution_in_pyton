from math import hypot
oposto = float(input('Digite o cateto oposto: '))
adjacente = float (input('Digite o cateto adjacente: '))
print('A hipotenusa vai medir: {:.2f}'.format(hypot(oposto, adjacente)))
