frase = str(input('Digite uma frase: ')).lower().replace(' ', '')
var = frase[::-1]
if frase == var:
    print('É palindromo')
else:
    print('Não é palindromo')
