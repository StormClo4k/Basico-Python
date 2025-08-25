# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# import dos metodos para calcular seno, cos e tangente
from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo desejado: '))

# A conversao do angulo para radiano é feita no momento do calculo do sen, cos e tan
print('O angulode de {} tem o seno de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O angulode de {} tem o cosseno de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O angulode de {} tem o tangente de {:.2f}'.format(angulo, tan(radians(angulo))))
