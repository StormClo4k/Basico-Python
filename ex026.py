#Exercício Python 26: Faça um programa que leia uma frase pelo teclado
#  e mostre quantas vezes aparece a letra “A”, em que posição ela aparece
#  a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uam frase: ')).strip()

print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a', 0, len(frase))))
print('A primeira letra A aparece na posicao {}'.format(frase.lower().find('a')))
print('A ultima letra A aparece na posicao {}'.format(frase.lower().rfind('a')))