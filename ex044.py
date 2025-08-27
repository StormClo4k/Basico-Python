# Exercício Python 44: Elabore um programa que calcule o valor
#  a ser pago por um produto, considerando o seu preço normal
#  e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor_compras = float(input('Digite o valor das suas comprar: '))
print('Opcoes de pagamento [1] à vista dinheiro/cheque')
print('Opcoes de pagamento [2] à vista no cartão')
print('Opcoes de pagamento [3] em até 2x no cartão')
print('Opcoes de pagamento [4] 3x ou mais no cartão')

pagamento = int(input('Digite o valor referente a forma de pagamento desejada: '))
if pagamento == 4:
    parcelas = int(input('Digite a quantidade das parlas: '))

if pagamento == 1:
    print('O valor a ser pago é {:.2f}'.format(valor_compras * 0.9))
elif pagamento == 2:
    print('O valor a ser pago é {:.2f}'.format(valor_compras * 0.95))
elif pagamento == 3:
    print('O valor a ser pago é {:.2f}, por parcela'.format(valor_compras / 2))
else:
    print('O valor a ser pago é de {:.2f}, dividido em {} parcelas'.format(valor_compras * 1.2 / parcelas, parcelas))
