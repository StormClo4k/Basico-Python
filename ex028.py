# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número
#  inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#  escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange

x = int(input('O computador vai escolher um nomero entre 0 e 5\n Digite o numero que voce acha que vai cair: '))
aleatorio = randrange(0, 5)

print('O numero escolhido está correto! Voce acertou!!' if x == aleatorio else 'Voce errou, o nume escolhido foi {}'.format(aleatorio))
