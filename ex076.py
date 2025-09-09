# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#  No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    "Arroz", 25.90,
    "Feijão", 8.50,
    "Macarrão", 6.20,
    "Óleo", 7.80,
    "Açúcar", 5.40,
    "Café", 18.90,
    "Leite", 4.70,
    "Manteiga", 9.30,
    "Pão", 7.00,
    "Refrigerante", 6.50
)

print('='*40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print('{:.<30}'.format(produtos[i]), end='')
    else:
        print(f'R$ {produtos[i]: >5}')
print('='*40)
