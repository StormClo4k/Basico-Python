# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

x = float(input('Digite a temperatuda que sera convertida: '))

print('A conversao dos graus C para F equivale a {:.1f}'.format(
    x * 9 / 5 + 32))
