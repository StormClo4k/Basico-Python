# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

x = int(input('Digite um valor para verificarmos se é impar ou par: '))

if x % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')
