# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem
#  em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
#  200Km e R$0,45 parta viagens mais longas.

km = int(input('Digite a distancia em kms da sua viagem: '))

if km <= 200:
    print('O valor da sua viagem é R${}!'.format(km * 0.5))
else:
    print('Voce obteve um desconto de 10% !! O valor da sua viagem é R${}!'.format(km * 0.45))
