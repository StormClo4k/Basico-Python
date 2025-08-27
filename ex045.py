# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randrange

maquina = randrange(1, 3)

print('Digite [1] = Pedra')
print('Digite [2] = Papel')
print('Digite [3] = Tesoura')

pessoa = int(input('escolha uma das 3 opcoes: '))


if maquina == pessoa:
    print('Empate!!')
elif pessoa == 1:
    if maquina == 3:
        print('Voce ganhou!! O resultado foi Pedra x Tesoura')
    else:
        print('Voce perdeu. A maquina escoheu Papel')
elif pessoa == 2:
    if maquina == 1:
        print('Voce ganhou!! O resultado foi Papel x Pedra')
    else:
        print('Voce perdeu. A maquina escoheu Tesoura')
else:
    print('Voce ganhou!! O resultado foi Tesoura x Papel,' if maquina == 2 else 'Voce perdeu. A maquina escoheu Pedra')
