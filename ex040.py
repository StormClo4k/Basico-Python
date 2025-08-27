# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira nota para o calculo da media: '))
nota2 = float(input('Digite sua segunda nota para o calculo da media: '))
media = (nota1 + nota2) / 2

print('Sua media foi {:.2f}'.format(media))

if media >= 7:
    print('APROVADO')
elif media >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')