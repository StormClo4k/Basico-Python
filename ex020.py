#  Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle # embaralha a lista

lista = ['Ana', 'Joao', 'Jose', 'Lucas']

shuffle(lista)

print(lista)