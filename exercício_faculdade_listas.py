# Exemplo Lista
numero = [1,2,3,4,5] #Listas
print(numero)

#Exemplo 2-
num = [1,2,3,4,5]
for n in num:
    if n % 2 == 0 :
        print(n ,'é par')
    else:
        print(n , 'é Ímpar')

nome = [1,2,3]
print(len(nome))

#Exemplo 3-
numu = [10,2,-23]
numu.append(5)
print(numu)

#Exemplo 4-
nume = [10,5,9]
del nume [1]
print(nume)

#Exercício 1- Faça um programa que tenha uma lista com 5 números positivos quaisquer e apresente a soma de todos os elementos.
positivo = [1,2,3,4,5]

soma = 0

for p in positivo:
    soma = soma + p
    
print("O resultado da soma é,", soma) 

#Exercício 2- Acrescente no programa anterior mais um elemento a lista e apresente (imprima) a lista com este novo elemento
#Exercício 3- Altere o programa 2 para que seja apagado o segundo elemento da lista
