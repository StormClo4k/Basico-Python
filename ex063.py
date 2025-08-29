# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
#  e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
x = 0
y = 1
cont = 0
cont_fim = int(input(
    'Digite a quantidade de termos que deseja ver na sequência de Fibonacci: '))

while cont != cont_fim:
    if cont % 2 == 0:
        print(x, end=' ')
        x += y
    else:
        print(y, end=' ')
        y += x
    cont += 1
print('Fim!')