# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot  # metodo para calcular a hipotenusa

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjasente: '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(co, ca)))
