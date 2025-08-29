# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

x = input('Digite o seu sexo, sendo M para homens e F para mulheres: ').upper()
while x != 'M' and x != 'F':
    x = input('Entrada invalida, digite novamente: ').upper()
