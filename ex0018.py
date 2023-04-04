from math import radians, sin, cos, tan
angu = float(input('Digite o valor do angulo: '))
radi = radians(angu)
print('O angulo de {} tem o SENO de {:.2f}'.format(angu, sin(radi)))
print('O Angulo de {} tem COSSENO de {:.2f}'.format(angu, cos(radians(angu))))
print('O Angulo de {} tem o TANGENTE de {:.2f}'.format(angu, tan(radi)))
