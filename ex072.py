num = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    x = int(input('Digite um valor de 1 a 20 para escreve-lo por extenso: '))
    if 1 <= x <= 20:
        break
    print('Tente novamente com um valor entre 1 e 20. ')

print(f'O numero digitado foi {num[x-1]}')
