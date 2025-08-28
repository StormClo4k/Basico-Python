# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
for i in range(0, 5):
    peso = float(input('Digite o peso da pessoa numero {}: '.format(i + 1)))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso

        elif menor > peso:
            menor = peso

print('Maior peso: {}Kg\nMenoir peso: {}Kg'.format(maior, menor))
