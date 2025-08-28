# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

maior = 0
menor = 0
now = datetime.now().year

for i in range(0, 7):
    x = int(input('Digite o ano de nascimento: '))
    if now - x >= 18:
        maior += 1
    else:
        menor += 1

print('Das 7 pessoas, {} são maiores de idade e {} são menores!'.format(maior, menor))
