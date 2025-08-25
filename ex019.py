# Exercício Python 19: Um professor quer sortear 
# um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos
# e escrevendo na tela o nome do escolhido.

n1 = str(input('Digite o nome de um aluno: '))
n2 = str(input('Digite o nome de um aluno: '))
n3 = str(input('Digite o nome de um aluno: '))
n4 = str(input('Digite o nome de um aluno: '))
lista = [n1, n2, n3, n4]

from random import choice

# choice escolhe um indice aleatorio dentro da lista
print('O aluno escolhido foi: {}'.format(choice(lista)))