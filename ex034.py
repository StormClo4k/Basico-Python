# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salario para o calculo de aumento: '))

if salario > 1250.00:
    print(
        f'O seu salario teve um aumento de 10%. O novo salario é de {salario * 1.1}')
else:
    print(
        f'O seu salario teve um aumento de 15%. O novo salario é de {salario * 1.15}')
