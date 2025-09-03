#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randrange
v = 0
while True:
    pc = randrange(0,10)
    num = int(input('Digite um numero: '))
    ixp = input('Impar ou par? [I/P]').strip().upper()[0]
    if (pc + num) % 2 == 0 and ixp == 'P':
        print(f'\nVoce colocou {num} dedos e a maquina {pc} dedos')
        print('Voce ganhou 1 ponto! Vamos jogar novamente')
        v += 1
    else:
        print(f'\nVoce colocou {num} dedos e a maquina {pc} dedos')
        print(f'Voce perdeu, tendo um total de {v} vitorias consecutivas.')
        break
