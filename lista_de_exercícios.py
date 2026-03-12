#VERIFICADOR DE IDADE-EXERCÍCIO 1
#Pergunta a idade ao usuário e o int transforma a string em um número.
idade = int(input("Qual é a sua idade?"))

if idade < 0:
    print("Idade incompatível.")
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#CALCULADORA SIMPLES-EXERCÍCIO 2
#Float vai transformar em decimal para realizar contas com pontos.
num_primeiro = float(input("Informe um número: ").replace(",", "."))

num_segundo = float(input("Informe outro número: ").replace(",", "."))
#se o usuários digitar vírgula, o replace irá trocar por ponto para o Python prosseguir.

resultado_soma = num_primeiro + num_segundo
resultado_mult = num_primeiro * num_segundo

print("A soma é: ", resultado_soma)
print("A multiplicação é: ", round(resultado_mult, 2))
# PESQUISA FEITA : FONTE OPENAI CHATGPT
# round() é usado para arredondar números decimais.
# cálculos com float podem gerar resultados com muitas casas decimais, pois os computadores não armazenam números decimais exatamente em binário e no sistema binário alguns números decimais também viram dízimas infinitas.
# Com round(valor, casas),podemos definir quantas casas decimais queremos mostrar.

#TEMPERATURA-EXERCÍCIO 3
temperatura = float(input("Qual é a temperatura?"))

if temperatura > 30:
    print("Está muito quente.")
    
elif 20 <= temperatura <= 30:
    print("Temperatura agradável.")

elif temperatura < 20:
    print("Está frio.")
