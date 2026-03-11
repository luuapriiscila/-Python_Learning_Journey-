# Tentativa de soma (problema com strings)
num1 = input('Escreva um número:')
num2 = input('Escreva outro número:')

print('A soma de',num1,'e',num2,'é',num1+num2)
# Não dá certo dessa forma somar, o operador + apenas junta as strings.

# Primeira tentativa de validação de número:
digitado = int(input('Digite um número:'))

if digitado == 2 or digitado == 5 or digitado == 6:
    print('Seu número foi aceito.')
else:
    print('Seu número não é válido.')

# Versão melhorada usando lista
digitado = int(input('Digite um número: '))

validos = [2, 5, 6]

if digitado in validos:
    print('Seu número foi aceito')
else:
    print('Seu número não é válido')
