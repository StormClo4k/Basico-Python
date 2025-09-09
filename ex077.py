# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
#  (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    "vento", "cacto", "espelho",
    "nuvem", "relogio", "ponte",
    "areia", "trilho", "oceano",
    "chave")

for palavra in palavras:
    print(f'\nA palavra {palavra}, tem as seguintes vogais:', end=' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
