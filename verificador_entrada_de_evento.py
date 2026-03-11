# pede ao usuário que digite seu nome
nome=input("Qual é o seu nome?")

# pede a idade do usuário e converte o valor para inteiro
idade=int(input("Qual é a sua idade?"))

# enquanto a idade for menor que 0, o programa considera inválida
while idade < 0:
    # mensagem informando que a idade é inválida
    print("Idade inválida.")
    # pede novamente a idade até que seja um valor válido
    idade=int(input("Qual é a sua idade novamente:"))
                    
# pergunta se o ingresso foi pago e transforma a resposta em minúscula
ingressoPago=input("Você pagou seu ingresso?(sim ou não):").lower()

# verifica se a resposta é diferente de "sim" ou "não"
# se for diferente, pede para o usuário digitar novamente
while ingressoPago not in ["sim","não"]:
    print('Por favor, coloque apenas "sim" ou "não".')
    ingressoPago=input("Seu ingresso foi pago?(sim ou não)").lower()
                                        
# verifica duas condições ao mesmo tempo:
# se a idade é maior ou igual a 18 E se o ingresso foi pago
if idade >= 18 and ingressoPago == "sim":
    # se as duas condições forem verdadeiras, a entrada é permitida
    print("Entrada permitida. Bem-vindo ao evento,",nome)
else:
    # caso alguma das condições não seja atendida, a entrada é negada

# Exercício de prática em Python
# Código refinado após revisão para melhorar organização e validação de entrada
    print("Entrada não permitida.")
