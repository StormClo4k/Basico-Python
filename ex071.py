# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Qual valor voce deseja sacar? R$'))

while True:
    if saque <= 0:
        saque = int(input('Valor escolhido é invalido, Digite outro valor: '))

    else:
        if saque >= 50:
            print(f'Total de {int(saque/50)} cedulas de R$50')
            saque = saque % 50
        elif saque >= 20:
            print(f'Total de {int(saque/20)} cedulas de R$20')
            saque = saque % 20
        elif saque >= 10:
            print(f'Total de {int(saque/10)} cedulas de R$10')
            saque = saque % 10
        elif saque >= 1:
            print(f'Total de {int(saque/1)} cedulas de R$1')
        break
