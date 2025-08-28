# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média
# de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

quant_m = 0
quant_f = 0
media_m = 0
media_f = 0
mais_velho = ''
mais_velho_anos = 0
menos_20_anos_f = 0

for i in range(0, 4):
    nome = input('Digite um nome: ').upper()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite M para masculino e F para feminino: ').upper()
    if sexo == 'M':
        media_m += 1
        quant_m += idade
        if idade > mais_velho_anos:
            mais_velho = nome
            mais_velho_anos = idade
    elif sexo == 'F':
        media_f += 1
        quant_f += idade
        if idade < 20:
            menos_20_anos_f += 1

print('Mulheres: {}, Media da idade: {}'.format(media_f, quant_f / media_f))
print('Homens: {}, Media da idade: {}'.format(media_m, quant_m / media_m))
print('Homen mais velho: {}, com {} anos'.format(mais_velho, mais_velho_anos))
print('Mulheres com menos de 20 anos: {}'.format(menos_20_anos_f))
