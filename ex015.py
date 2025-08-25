# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = int(input('Digite a quantidade de KM percorrida: '))

d = d * 60
km = 0.15 * km

print('O valor a ser pago é de {}'.format(d+km))
