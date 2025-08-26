# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano para verificarmos se é bicesto: '))

if ano % 4 == int:
    print('O ano é bicesto')
elif ano % 100 == 0 and ano % 400 == int:
    print('O ano é bicesto')
else:
    print('O ano não é bicesto')
