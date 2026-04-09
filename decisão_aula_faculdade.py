#Leia um número inteiro e informe se ele é positivo, negativo ou zero
numero = int(input("Informe um número:"))

if numero > 0:
    print("Esse número é positivo")
elif numero == 0:
    print("Seu número é igual a zero")
else:
    print("Seu número é negativo")

#Leia um número inteiro e verifique se ele é par ou ímpar
numero1 = int(input("Informe um número para verificar se é ímpar ou par:"))
if numero1 % 2 == 0:
    print("Seu número é par.")
else:
    print("Seu número é ímpar")

#Leia a idade de uma pessoa e informe se ela é maior ou menor de idade(18 anos)
idade = int(input("Qual a sua idade?"))

if idade > 18:
    print("Você é maior de idade.")
elif idade == 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#Leia o valor de uma compra. Se o valor for maior que R$100, aplique 10% de desconto
compra = float(input("Qual o valor da sua compra?"))

desconto = compra*0.1
precofim = compra - desconto

if compra > 100:
    print("O valor da sua compra é", precofim)
else:
    print("O valor da sua compra não recebeu desconto.")


#Leia duas notas, calcule a média e informe: Aprovado (média ≥ 7), Recuperação (média ≥ 5 e < 7) e Reprovado (média < 5)
nota_1 = float(input("Informe sua nota:"))
nota_2 = float(input("Informe outra nota:"))

media = (nota_1+nota_2)/2

if media >= 7:
    print("Aprovado.")
elif 5 <= media < 7:
    print("Recuperação")
elif media < 5:
    print("Reprovado")
