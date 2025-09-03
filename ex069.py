'''Exercício Python 69: Crie um programa que leia a idade e o sexo
 de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
   se o usuário quer ou não continuar. No final, mostre:'''
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

a = b = c = 0
continua = ''

while True:
    if continua == 'N':
        break
    else:
        idade = int(input('Idade: '))
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        print('-'*20)

        continua = input('Quer continuar? [S/N]').strip().upper()[0]
        while continua not in 'SN':
            continua = input('Quer continuar? [S/N]').strip().upper()[0]
            print('-'*20)

        if sexo == 'M':
            b += 1
        elif idade > 18:
            a += 1
            if idade < 20 and sexo == 'F':
                c += 1
print(f'quantas pessoas tem mais de 18 anos: {a}')
print(f'quantos homens foram cadastrados: {b}')
print(f'quantas mulheres tem menos de 20 anos: {c}')
