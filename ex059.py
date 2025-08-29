'''#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

x1 = float(input('Digite o primeiro numero: '))
x2 = float(input('Digite o segundo numero: '))

while True:
    opcao = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa \n'))
    if opcao not in range(1,5):
       print('Opcao invalida! encerrando programa')
       break
    match opcao:
        case 1:
          print('A soma equivale a ',x1 + x2)
        case 2:
          print('A multiplicacao equivale a ',x1 * x2)
        case 3: 
          print('O maior é',x1 if x1 >= x2 else 'O maior é',x2)
        case 4:
            x1 = float(input('Digite o primeiro numero: '))
            x2 = float(input('Digite o segundo numero: '))
        case 5:
            print('Saindo')
            break
