# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
#  acrescentando o recurso de mostrar que tipo de triângulo
#  será formado:

# equilátero se os três lados tiverem o mesmo comprimento,
#  isósceles se dois lados forem iguais e o terceiro for diferente,
#  e escaleno se todos os três lados tiverem comprimentos distintos.

l1 = float(input('Digite o lado 1 do triangulo: '))
l2 = float(input('Digite o lado 2 do triangulo: '))
l3 = float(input('Digite o lado 3 do triangulo: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Nao é possivel formar um triangulo!!')
else:
    print('É possivel formar um triangulo!!')
    if l1 == l2 and l2 == l3:
        print('Seu triangulo é EQUILATERO!')
    elif l1 != l2 and l2 != l3:
        print('Seu triangulo é ESCALENO')
    else:
        print('Seu triangulo é ISOCELES')
