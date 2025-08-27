# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para
#  a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite o seu salario: '))
tempo = int(input('Em quantos anos pretende pagar: '))

prestacao = valor_casa / (tempo * 12)

if prestacao > salario * 0.3:
    print('Seu empréstimo não foi aprovado, pois o valor da prestação mensal não pode exceder 30% do salário')
else:
    print('Seu empréstimo foi aprovado! o valor da prestação mensal é de {:.2f}'.format(prestacao))
