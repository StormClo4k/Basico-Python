# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc  # trunc é o metodo para ver a parte inteira de uma variavel

x = float(input('Digite um numero real: '))
print('O numero real mais proximo de {} é {}'.format(x, trunc(x)))
