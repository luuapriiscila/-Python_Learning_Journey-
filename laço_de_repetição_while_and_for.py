# |Exercício 1:Mostre os números de 0 até 10
for i in range(11):
    print(i)
  
# |Exercício 2: Mostre os números de 1 até 10
for i in range(1,11):
    print(i)
  
# |Exercício 3: Mostre apenas números pares de 0 até 20
for i in range(0,21,2):
    print(i)
  
# |Exercício 4: Peça um número ao usuário e mostre a tabuada dele
numero = int(input("Informe um número:"))

for i in range(1,11):
    print(numero,"x",i,"=", numero*i)
  
# |Exercício 5: (desafio) Some todos os números de 1 até 100
soma = 0

for i in range(1,101):
    soma = soma + i

print("O resultado é:", soma)

