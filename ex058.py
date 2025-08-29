#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o 
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randrange
palpite = 0
aleatorio = randrange(0, 5)

x = int(input('O computador vai escolher um nomero entre 0 e 5\n Digite o numero que voce acha que vai cair: '))
if x != palpite:
    print('Voce errou, o numero escolhido foi {}\n'.format(aleatorio))
while x != aleatorio:
    x = int(input('Digite outro valor para tentar novamente: '))
    palpite += 1
    aleatorio = randrange(0, 5)
    print('Voce errou, o numero escolhido foi {}\n'.format(aleatorio))

print('O numero escolhido está correto! Voce acertou!!')
print('Fim')